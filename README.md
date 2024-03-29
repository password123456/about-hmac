# HMAC Examples
![made-with-python][made-with-python]
![Python Versions][pyversion-button]
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fhmac-examples&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg

An Example Implementation of Basic HMAC (Hash-based Message Authentication Code) Using Flask in Python.


# What is HMAC?!
Hash-based message authentication code (HMAC) provides the server and the client each with a private key that is known only to that specific server and that specific client. The client creates a unique HMAC, or hash, per request to the server by hashing the request data with the private keys and sending it as part of a request. What makes HMAC more secure than Message Authentication Code (MAC) is that the key and the message are hashed in separate steps.

![img](https://github.com/password123456/hmac-examples/blob/main/hmac.png)


# Example

## (1) Client Request to Server
- When a client sends a request to the server, it includes the following headers:

- `X-Authorization-Content-HMAC`: HMAC hash (Entire Request URI, Current Unix Timestamp(UTC), and HMAC Secret key)
- `X-Authorization-Timestamp`: Client current Unix Timestamp(UTC)

```
(request)
GET /example/users?user=test&institutionID=999&signature=7e745d74b69b7f62e8e2 HTTP/1.1
Host: example.com
X-Authorization-Content-HMAC: 1c73495878ccea24af9dd281a4c883c40a3551ba799d30f4ad7d9afb6a60fbd4
X-Authorization-Timestamp: 1711662980
```

[ Client Request Process ]
- The client prepares and sends the request to the server.
- The server validates the request by verifying the HMAC integrity and timestamp validity.
- If the validation succeeds, the server processes the request; otherwise, it sends an error response.

## (2) Server Response to Client
- When the server responds to a valid request, it includes the following headers:

- `X-Response-Content-HMAC`: HMAC hash (Entire response body, Current Unix Timestamp(UTC), and HMAC Secret key)
- `X-Response-Content-TimeStamp`: Current Unix Timestamp(UTC)

```
(response)
HTTP/2 200 OK
Date: Fri, 29 Mar 2024 06:50:49 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 52
X-Response-Content-HMAC: 529c33aac3e33bf2a95d534f8b3ac61dee2ed79232d729e571dc669417a1a2ae
X-Response-Content-TimeStamp: 1711663027
Connection: close

{"result": "ok", "users": "test", "sub": 2840345654}
```

[ Response Process ]
- The server prepares and sends the response data to the client.
- (Additional) If necessary, the client can verifies the HMAC integrity of the response data.
- If the validation fails, the client rejects the response data.
```
Server response HMAC verification successful
--------------
Response timestamp: 2024-03-29T09:25:31
Current time: 2024-03-29T09:25:31
Time difference: 0
```

# Additional Notes
- There's no strict rule on whether to use GET or POST; however, POST is commonly preferred for security reasons. Using GET requests can lead to all query strings being logged in web access logs
- Always use UTC Unix Timestamp for timestamp information to ensure consistency and avoid timezone-related issues.
- The scope of HMAC calculation can vary. While it typically involves hashing the entire response body, selective hashing of data is also possible, especially when the response body is extensive.
- The choice of HMAC algorithm (e.g., Hmac-SHA256, Hmac-SHA512) and the secret key length should be based on security requirements and best practices.

## Replay Requets Prevention
- The server can store processed requests in memory (e.g., Redis) and discard repeated requests within a specific time frame to prevent replay attacks.
- Additionally, the server can enhance replay attack prevention by comparing the timestamp header (X-Authorization-Timestamp) sent by the client in the request header with the current server time. If the timestamp falls outside a certain timeframe, the server can discard the request.

## And...
If you find this helpful, please the "star"🌟 to support further improvements.
