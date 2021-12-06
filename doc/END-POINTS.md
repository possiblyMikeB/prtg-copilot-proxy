# Available End-Points
## GET /pmapi/fetch 
### Description

This end-point triggers the corresponding end-point on the `pmproxy` server, records it's outcome and converts the results to a form meeting the vauge specification [found here](https://www.paessler.com/manuals/prtg/custom_sensors#advanced_sensors).

### Arguments

#### `hostspec`  (required) 

Valid `pcp` host specification; in particular must identify a host with an active instance of `pmcd`, and specify how to connect to said instance.  For details and further reading: Section of [PCPIntro](https://man7.org/linux/man-pages/man1/PCPIntro.1.html#PMCD_HOST_SPECIFICATION) titled "PMCD HOST SPECIFICATION"

**Note**: In most cases, the hostname of a sever running a properly configered instance of `pmcd` suffices. 

#### `names` (required)

A comma seperated list of valid PCP metrics which are observable on the host specified in `hostspec`. What metrics are available can vary from host to host based on several factors. For a list of some of the available metrics, see `METRICS.md`.

### Examples

In this example we will fetch the current values for the metrics `nvidia.temp` and `kernel.all.load` from the server `gpu0`, for this request our parameters will be `hostspec=gpu0` and `names=nvidia.temp,kernel.cpu.util.idle`. Assuming the service is available at `https://metrics-host:8888` the request URL is:

```
https://metrics-host:8888/pmapi/fetch?hostspec=gpu0&names=nvidia.temp,kernel.all.load
```

with the following response

```json
{
  "prtg": {
    "result": [
      {
        "channel": "Nvidia Temp 0",
        "value": 25,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Nvidia Temp 1",
        "value": 27,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Nvidia Temp 2",
        "value": 25,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Nvidia Temp 3",
        "value": 27,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Nvidia Temp 4",
        "value": 27,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Nvidia Temp 5",
        "value": 27,
        "unit": "Custom",
        "customunit": "C"
      },
      {
        "channel": "Kernel All Load 1",
        "value": 28.84
      },
      {
        "channel": "Kernel All Load 5",
        "value": 18.75
      },
      {
        "channel": "Kernel All Load 15",
        "value": 8.3100004
      }
    ],
    "message": "OK",
    "error": 0
  }
}
```
