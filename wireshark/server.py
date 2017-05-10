from http.server import HTTPServer, BaseHTTPRequestHandler
#import ssl

# This handler says MEOW to all GET requests
class MeowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("MEOW!".encode("utf-8"))

server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, MeowHandler)
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
