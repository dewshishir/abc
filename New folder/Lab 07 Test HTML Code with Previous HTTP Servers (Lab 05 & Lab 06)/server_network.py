from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"   # Accessible from network
PORT = 8000

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    print(f"Network Server Running at http://localhost:{PORT}")
    print("Accessible from other devices in same network")

    httpd.serve_forever()

if __name__ == "__main__":
    run()
