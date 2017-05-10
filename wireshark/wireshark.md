```python
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
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True, ciphers='RSA')
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
```

---

- `https://localhost:4443?query=something`
- `sudo tcpdump -i lo0 -s 0 tcp port 4443 \
 -w localhost.pcap`
- we can see the request and response!

---

(now with SSL)

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

# This handler says MEOW to all GET requests
class MeowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("MEOW!".encode("utf-8"))

server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, MeowHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True, ciphers='RSA')
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
```

---

```bash
# make a public key signed by itself ("self-signed certificate")
openssl req -new -x509 -out selfsigned.crt -nodes -keyout selfsigned.key -subj /O=Recurse/CN=localhost

# base64-encoding of a ASN.1-formatted file (similar in concept to JSON)
openssl asn1parse -i -in selfsigned.crt

# more helpful output format (look for `notBefore`, `notAfter`)
openssl x509 -in selfsigned.crt -text -noout

# manpages are tricky to find
man req
man x509
```

---

- `https://localhost:4443?query=something`
- `sudo tcpdump -i lo0 -s 0 tcp port 4443 \
 -w localhost.pcap`
- we can't see the request or response! (:smile: or :cry: depending on what you want)
