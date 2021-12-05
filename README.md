  # PRTG Performance Co-Pilot Proxy 
  
  This repository contains a small web-service which converts the REST API used by [`pmproxy`](https://man7.org/linux/man-pages/man1/pmproxy.1.html) (part of
  [`pcp`](https://pcp.io/)) into something that can be consumed by PRTG's "HTTP Data Advanced" sensor. 

## Required Infrastructure

  Before using this service, you will need the following
  
   * A server providing a working instance of the `pmproxy` HTTP service (we'll use `metrics-host` to refer to this server)
   * Any server whose metrics you'd like to montior will need
     * [`pmcd`](https://man7.org/linux/man-pages/man1/pmcd.1.html) service enabled & running.
     * `pmcd` configured to only allow remote metric query's from the host `metrics-host.` 
     * `pmcd` to strictly enfroce TLS based authentication.
   * A trusted `CA` to issue the (required) pair of TLS certificates (a server certificate for the service and a client certificate to install in PRTG.)

