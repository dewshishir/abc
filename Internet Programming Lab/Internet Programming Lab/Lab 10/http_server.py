from http.server import HTTPServer, SimpleHTTPRequestHandler

class ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True

HOST = "127.0.0.2"
PORT = 8080

server = ReusableHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("Website running for csebatcheight3052.com")
print(f"Open: http://csebatcheight3052.com:{PORT}")

server.serve_forever()

