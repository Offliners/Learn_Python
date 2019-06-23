# creating a simple web server that
# servers the contents of the directory
# and displays files

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ("",5000),handler) as httpd:
    # ^ ip (all ips)
    #   ^ port
    httpd.serve_forever()

# Output:
# 127.0.0.1 - - [23/Jun/2019 11:43:43] "GET / HTTP/1.1" 200 -
