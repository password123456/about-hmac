# HMAC Examples
![made-with-python][made-with-python]
![Python Versions][pyversion-button]
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fhmac-examples&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
An example implementation of HMAC (Hash-based Message Authentication Code) using Flask in Python. 


## What is HMAC?!
Hash-based message authentication code (HMAC) provides the server and the client each with a private key that is known only to that specific server and that specific client. The client creates a unique HMAC, or hash, per request to the server by hashing the request data with the private keys and sending it as part of a request. What makes HMAC more secure than Message Authentication Code (MAC) is that the key and the message are hashed in separate steps.

