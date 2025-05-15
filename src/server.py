import socketserver
import ssl
import http.server

# defining the port
PORT = 5678 


# tuple containing server_name localhost by default, and server_port
server_address = ('', PORT)
# handler handling upcoming client requests
handler = http.server.SimpleHTTPRequestHandler

# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('../cert.pem', '../domain.key')

with socketserver.TCPServer(server_address, handler, True) as httpd:
    print(f"server opened port: {PORT}")
    # telling our server to use certificate
    httpd.socket = context.wrap_socket(httpd.socket, True)
    # server the http server forever
    httpd.serve_forever()