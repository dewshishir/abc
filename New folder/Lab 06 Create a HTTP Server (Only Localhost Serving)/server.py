from http.server import HTTPServer, SimpleHTTPRequestHandler

# Bind only to localhost
HOST = "127.0.0.1"   # Localhost only
PORT = 8080          # You can change port if needed

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    print(f"Server running at http://{HOST}:{PORT}")
    print("Accessible only from this computer.")
    print("Press CTRL + C to stop.")

    httpd.serve_forever()

if __name__ == "__main__":
    run()
