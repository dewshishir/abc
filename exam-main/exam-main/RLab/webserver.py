

from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

WEB_PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

LOCAL_IP = get_local_ip()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>csebatcheight1005.com</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: rgba(0,0,0,0.3);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        h1 { font-size: 2.5em; margin-bottom: 10px; }
        h2 { font-size: 1.3em; color: #ddd; font-weight: normal; }
        .info { margin-top: 30px; font-size: 1.1em; line-height: 2; }
        .domain { color: #ffd700; font-weight: bold; font-size: 1.2em; }
        .success { color: #00ff88; font-size: 1.5em; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to CSE Batch Eight</h1>
        <h2>Registration Number: 1005</h2>
        <p class="success">&#10004; Site Successfully Accessed via Local DNS!</p>
        <div class="info">
            <p>Domain: <span class="domain">csebatcheight1005.com</span></p>
            <p>Lab 10: Access the Site with Local DNS Server</p>
            <p>Server IP: """ + LOCAL_IP + """</p>
            <p>DNS Port: 9953 | Web Port: 8080</p>
        </div>
    </div>
</body>
</html>
"""

class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

    def log_message(self, format, *args):
        print(f"   [WEB] {self.client_address[0]} requested {self.path}")

print("=" * 60)
print("   Lab 10: WEB SERVER for csebatcheight1005.com")
print("=" * 60)
print(f"   Serving on http://{LOCAL_IP}:{WEB_PORT}")
print(f"   Also available at http://127.0.0.1:{WEB_PORT}")
print("=" * 60)
print("\n   Waiting for HTTP requests...\n")

server = HTTPServer(("0.0.0.0", WEB_PORT), LabHandler)
server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.serve_forever()
