![inline](images/client-server-communication.gif)

[.footer: http://sureshatt.blogspot.com/2010/10/simple-web-application.html]

---

(our test server responds MEOW to every GET request)

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

# In the browser

![inline](images/in-the-browser.png)

---

# Beyond the browser

tcpdump +

![inline fill](images/wireshark-logo.png)

useful for:

- learning about networking
- debugging

---

# Plaintext (http)

```bash
sudo tcpdump -i lo0 -s 0 tcp port 4443 -w localhost.pcap
```

![inline](images/localhost-http-wireshark.png)

---

(same test server now with SSL)

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

# Where do I get the SSL certificate?

```bash
# make a private key, and public key signed by itself ("self-signed certificate")
openssl req -new -x509 -out selfsigned.crt -nodes -keyout selfsigned.key -subj /O=Recurse/CN=localhost

-----BEGIN CERTIFICATE-----
MIIDHzCCAgegAwIBAgIJAOwd/WUEg+/SMA0GCSqGSIb3DQEBCwUAMCYxEDAOBgNV
BAoMB1JlY3Vyc2UxEjAQBgNVBAMMCWxvY2FsaG9zdDAeFw0xNzA1MTAxNjUxMDZa
(...)
GwDgu2nix1sQ97fEXyRn9HqIQh8yzBjMc/splbi0yOCzbmV0iHUKFFPKUhx4+7St
LQdq6xAf5xwZyIjdd91OdyMfu/QVzkUuwXA8RMQq1ncHhQI=
-----END CERTIFICATE-----

-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDd0YuYRsgT/Q7/
nIxrnRsDulVFqpWa/lFnwyyhi7geCYZCVgrgM18OnDUCy59nybxUs7IcdO6EcU71
(...)
0uuuJzD/GyhzJgivVF3nbCdSr25DlRrEEThD+MFm3eo0cIKFXVmV6DH7pTZMBA13
+A5FylQkyuWk8vQDEO6uEFw5
-----END PRIVATE KEY-----



# helpful output format
openssl x509 -in selfsigned.crt -text -noout

Certificate:
    (...)
    Issuer: O=Recurse, CN=localhost
    Validity
        Not Before: May 10 16:51:06 2017 GMT
        Not After : Jun  9 16:51:06 2017 GMT
    Subject: O=Recurse, CN=localhost
    (...)
```

---

# Encrypted (https)

```bash
sudo tcpdump -i lo0 -s 0 tcp port 4443 -w localhost.pcap
```

![inline](images/localhost-https-wireshark.png)

---

# Getting the "base color" for Diffie-Helman

```bash
export SSLKEYLOGFILE=~/RC/lightning-talks/wireshark/keys/sslkeylog.log
```

---

# Decrypted (https)

```bash
sudo tcpdump -i lo0 -s 0 tcp port 4443 -w localhost.pcap
```

![inline](images/localhost-https-wireshark.png)
