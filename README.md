# HMAC Examples
![made-with-python][made-with-python]
![Python Versions][pyversion-button]
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fhmac-examples&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
An example implementation of HMAC (Hash-based Message Authentication Code) using Flask in Python. 


## What is HMAC?!
Hash-based message authentication code (HMAC) provides the server and the client each with a private key that is known only to that specific server and that specific client. The client creates a unique HMAC, or hash, per request to the server by hashing the request data with the private keys and sending it as part of a request. What makes HMAC more secure than Message Authentication Code (MAC) is that the key and the message are hashed in separate steps.

## Example - Request / Response 

```
(request)
GET /example/users?user=test&institutionID=999&signature=7e745d74b69b7f62e8e2 HTTP/1.1
Host: example.com
X-Request-HMAC: 1c73495878ccea24af9dd281a4c883c40a3551ba799d30f4ad7d9afb6a60fbd4
X-Request-TimeStamp: 1711662980


(response)
HTTP 1.1 200 OK
Date: Fri, 29 Mar 2024 06:50:49 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 52
X-Response-Content-HMAC: 529c33aac3e33bf2a95d534f8b3ac61dee2ed79232d729e571dc669417a1a2ae
X-Response-Content-TimeStamp: 1711663027
Connection: close


{"result": "ok", "users": "test", "sub": 2840345654}

```

## Server Response Verification
```
Server response HMAC verification successful
--------------
Response timestamp: 2024-03-29T06:57:07
Current time: 2024-03-29T06:57:07
Time difference: 0
```
