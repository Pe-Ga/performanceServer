# Specs of jsonServer-API

## Function */hello*
Basic function to check if the server is up and running.

**HTTP method**: `GET`

**Parameters**: 
* None

**Response**:
* HTTP status code: `200` (OK)
* HTTP body: 
> Hello World!

## Function: /getdata
Returns performance data in a specified 5 minute slice.

**HTTP method**: `GET`

**Parameters**:
* *time* (required)

The UNIX epoch time of the requested time slice.

Note that the server only holds data not older than 3 days and only for time slices which are integer multiples of 5 minutes (300 seconds). Also, *time* should not be younger than `(now - 5min)`, data may not be present. *time* may not be present or future.

**Response**

**If valid *time* parameter provided:**
* HTTP status code: `200` (OK)
* HTTP body: A multiple of pipe seperated performance data (including headings)

`Timestamp|Duration|Key|[Name of values|]*`

> Timestamp|Duration|Key|CPU|Power|
>
> 1649956500000000|5|mykey20761|0.8303407860710061|0.8502794295515399
>
> 1649956500000000|5|mykey21474|0.5925113789730341|0.1781359588191057

Caution! The first line containing headings for the CSVish data contains more seperators than columns. This lead to confusion for some CSV readers recently.

**If the *time* parameter provided is invalid:**

*parameter *time* omitted*
* HTTP status code: `400` (Bad Request)
* HTTP body:
> the time paramter is missing or wrong  query=

*parameter *time* is not an epoch time*
* HTTP status code: `400` (Bad request)
* HTTP body:
> NumberFormatException thrown

*parameter *time* is not a multiple of 5 minutes*
* HTTP status code: `400` (Bad request)
* HTTP body:
> time is not at 5 minutes interval  time= [value provided in parameter time in seconds]

*parameter *time* is older than 3 days*
* HTTP status code: `400` (Bad request)
* HTTP body:
> time is too much in the past more than 3 days  time= [value provided in parameter time in millis]

*parameter *time* is too young (i.e. too close to present or in the future)*
* HTTP status code: `400` (Bad request)
* HTTP body:
> time is in the future   time= [value provided in parameter time in millis]


