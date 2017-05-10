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
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
```

---

tcpdump on **localhost** (`-i lo0`) **port 4443**, **show full packets** (`-s 0`)

```bash
sudo tcpdump -i lo0 -s 0 tcp port 4443 -w localhost-http.pcap
```

https://localhost:4433?query=something

We can see the request! And the response!

---

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
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='selfsigned.key', certfile='selfsigned.crt', server_side=True)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
```

---

```bash
openssl req -new -x509 -out selfsigned.crt -nodes -keyout selfsigned.key -subj /O=Recurse/CN=localhost
man req
```

base64-encoding of a ASN.1-formatted file (similar in concept to JSON)
```bash
openssl asn1parse -i -in mysterious_file.pem
```

more helpful output format (look for `notBefore`, `notAfter`)
```bash
openssl x509 -in server.crt -text -noout
man x509
```

---

tcpdump on **localhost** (`-i lo0`) **port 4443**, **show full packets** (`-s 0`)

```bash
sudo tcpdump -i lo0 -s 0 tcp port 4443 -w localhost-https.pcap
```

https://localhost:4433?query=something

We can't see the request or response ( :( or :) depending on what you want)

---

`wireshark --version` (look for GnuTLS - SSL decryption support)
4443 -> HTTP/SSL settings


Look at the handshake pattern: rsa-only, or DH.
