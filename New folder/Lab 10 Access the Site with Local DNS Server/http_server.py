from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

HOST = "0.0.0.0"
PORT = 80

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEBSITE_DIR = os.path.join(BASE_DIR, "website")

os.chdir(WEBSITE_DIR)

httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("HTTP Server Running on Port 80")
httpd.serve_forever()

