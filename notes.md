# Building an http server in python

## Basic usage:
- it waits for requests from the client as an example (GOOGLE CHROME), servers files as an example as a response.
- it can handle only one request at the time or even handle more.

## ```http.server``` module:
- This module defines classes for implementing HTTP servers.
- but as the docs suggests it is not recommended to use it in production, cause it is not that secured.

## HTTPServer:
- it is a subclass of socketserver.TCPServer: they use TCP connection cause it is more reliables not the fastest method but reliable, it ensures requests and responds arrive.
- it automatically creates HTTP sockets and listens for requests, and dispatch the requests to a handler.

- ***Example***:
  ```python
    def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
    ```
- it is built on top of the TCPServer class, it stores server adress as instance variables, server_name and server_port, and also the handler as an instance variable.
- We should have an instance of handler_class upon each request.

## OPENSSL:
- Generating a Private key and csr to secure out server.
- the CSR generated can be sent to certificate authority, they are responsible for ssl cetificates.
- Private key and csr generation.

```
openssl req \
       -newkey rsa:2048 -nodes -keyout something.key \
       -out something.csr
```

***Self-signed*** no need to wait for CA, only for local use.
```
openssl req -new -x509 -key your.key -out cert.pem -days 365
```