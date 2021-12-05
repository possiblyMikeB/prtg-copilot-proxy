# Available End-Points
## GET /pmapi/fetch 
### Description

This end-point triggers the corresponding end-point on the `pmproxy` server, records it's outcome and converts the results to a form meeting the vauge specification [found here](https://www.paessler.com/manuals/prtg/custom_sensors#advanced_sensors).

### Arguments
#### `hostspec`  (required) 

Valid `pcp` host specification; in particular must identify a host with an active instance of `pmcd`, and specify how to connect to said instance.  For details and further reading: Section of [PCPIntro](https://man7.org/linux/man-pages/man1/PCPIntro.1.html#PMCD_HOST_SPECIFICATION) titled "PMCD HOST SPECIFICATION"

**Note**: In most cases, the hostname of a sever running a properly configered instance of `pmcd` meeting the assumptions mentioned in the `README.md` of this repository suffices. 

#### `names` (required)

A comma seperated list of valid PCP metrics which are observable on the host specified in `hostspec`. These 
