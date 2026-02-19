import http.server
import socketserver
import os

HOST = "127.0.0.1"
PORT = 3063

class joy_HTMLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            if os.path.exists('index.html'):
                print(f"[Joy_Log] Serving index.html to {self.client_address}")
            else:
                print(f"[Joy_Log] index.html not found! Serving directory list.")
        super().do_GET()

def joy_run_test_server():
    with socketserver.TCPServer((HOST, PORT), joy_HTMLHandler) as httpd:
        print(f"--- Joy's Test Server Running ---")
        print(f"URL: http://{HOST}:{PORT}")
        print(f"Serving files from: {os.getcwd()}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by Joy.")
            httpd.server_close()

if __name__ == "__main__":
    joy_run_test_server()