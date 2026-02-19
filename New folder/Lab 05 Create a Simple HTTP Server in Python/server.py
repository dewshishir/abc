from http.server import HTTPServer, SimpleHTTPRequestHandler

# Server configuration
HOST = "0.0.0.0"   # Listen on all available interfaces
PORT = 8000        # You can change port if needed

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"Server running at http://localhost:{PORT}")
    print("Press CTRL + C to stop the server")
    
    httpd.serve_forever()

if __name__ == "__main__":
    run()
