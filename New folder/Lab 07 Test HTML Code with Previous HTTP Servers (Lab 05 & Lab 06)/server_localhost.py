from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"   # Localhost only
PORT = 8080

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    print(f"Local Server Running at http://{HOST}:{PORT}")
    print("Accessible only from this computer")

    httpd.serve_forever()

if __name__ == "__main__":
    run()
