# HMAC Examples
An example implementation of HMAC (Hash-based Message Authentication Code) using Flask in Python. 

## What is HMAC?!
Hash-based message authentication code (HMAC) provides the server and the client each with a private key that is known only to that specific server and that specific client. The client creates a unique HMAC, or hash, per request to the server by hashing the request data with the private keys and sending it as part of a request. What makes HMAC more secure than Message Authentication Code (MAC) is that the key and the message are hashed in separate steps.

