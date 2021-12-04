#!/usr/bin/env python

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import requests, json, functools
from tornado.options import define, options

@functools.lru_cache(maxsize=None)
def get_instances(series_id):
    res = requests.get(
        f'{options.proxy_host}/series/instances',
        params={'series': series_id}
    )
    res.raise_for_status()

    print(res.json())
    response = res.json()
    if not isinstance(response, list):
        raise Exception("unknown error")
    
    return response


@functools.lru_cache(maxsize=None)
def get_sources(source_id):
    res = requests.get(
        f'{options.proxy_host}/series/sources',
        params={'source': source_id}
    )
    res.raise_for_status()

    print(res.json())
    response = res.json()
    if not isinstance(response, list):
        raise Exception("unknown error")
        
    for item in response:
        if (item['source'] == source_id) and \
           (item['name'].endswith(options.domain)):
            return item['name']
            
    raise Exception("HTTP Response missing series entry")

    
class PRTGHandler(tornado.web.RequestHandler):
    def write_json(self, obj):
        self.add_header('Content-Type', 'application/json')
        self.write(json.dumps(obj))

    def write_result(self, result):
        self.write_json({
            "prtg": {
                "result": result,
                "message": "OK",
                "error": 0
            }
        })
    
    def error_json(self, message):
        self.write_json({
            'prtg': {
                'error': 1,
                'text': message
            }
        })


class FetchHandler(PRTGHandler):
    def get(self):
        # both of these are required
        params = {
            'hostspec': self.get_argument('hostspec'),
            'names': self.get_argument('names')
        }
        
        res = requests.get(f'{options.proxy_host}/pmapi/fetch', params=params)
        if res.status_code != 200:
            # if the request didn't succed then report the error to PRTG
            self.error_json("HTTP Request to PMPRoxy failed.")
            return
        
        # get the result's json content
        response = res.json()
        
        # initialize response 'results' objects
        results = list()
        
        # loop through returned metrics and generate
        # entries appropriate for `obj.prtg.result`
        for item in response.get('values'):
            base_name = ' '.join(item.get('name').split('.')).title()
            for val in item.get('instances'):
                robj = {
                    'channel': f'{base_name} {val.get("instance")}',
                    'value': val.get('value')
                }
                if item.get('name').endswith('temp'):
                    robj['unit'] = 'Custom'
                    robj['customunit'] = 'C'
                    pass
                results.append(robj)
                pass
            
        self.write_result(results)
        pass
    pass


class SeriesHandler(PRTGHandler):
    def get(self):
        # extra relavent arguments
        params = {
            'expr': self.get_argument('expr')
        }

        res = requests.get(f'{options.proxy_host}/series/query', params=params)
        if res.status_code != 200:
            # relay error to PRTG
            self.error_json(f'Failed request Status: {res.status_code}')
            return

        # process response and build results obj
        response = res.json()
        robj = list()
        hosts = dict()
        for ii, item in enumerate(response):
            value = item.get('value')
            sid = item.get('series')
            
            # get hostname from series labels
            inst = get_instances(sid)
            host = get_sources(inst[0]['source']).split('.')[0]
            hosts[host] = hosts.get(host, 0)
            name = [obj['name'] for obj in inst if obj['id'] == hosts[host]]
            name = name[0]
            robj.append({
                'channel': f'{name} ({host})',
                'value': value
            })
            hosts[host] += 1
            pass
        self.write_result(robj)
            
    pass



# tornado appliation 
application = tornado.web.Application(
    [
        (r"/pmapi/fetch",  FetchHandler),
        (r"/series/query", SeriesHandler)
    ]
)
