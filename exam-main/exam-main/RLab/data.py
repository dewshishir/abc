# code for Lab report 1:Implement and establish Socket Client-Server Communication in Python
# server code:
import socket
import threading
HOST = "0.0.0.0"
PORT = 1005
def handle_client(conn: socket.socket, addr):
	print(f"[+] New connection from {addr}")
	try:
		while True:
			data = conn.recv(4096)
			if not data:
				break
			message = data.decode("utf-8")
			print(f"[{addr[0]}:{addr[1]}] {message}")
			conn.sendall(data)
	except (ConnectionResetError, BrokenPipeError):
		pass
	finally:
		conn.close()
	print(f"[-] Connection closed: {addr}")
print(f"Starting echo server on Url {HOST} with {PORT} port...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((HOST, PORT))
	server_socket.listen()
	print("Server is listening...")
	while True:
		conn, addr = server_socket.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.daemon = True
		thread.start()

# client code:
import socket
import sys
HOST = "127.0.0.1" 
PORT = 1005
def start_client():
	try:
		with socket.create_connection((HOST, PORT), timeout=10) as sock:
			print(f"[+] Connected to {HOST}:{PORT}")
			print("Type your messages (empty line or Ctrl+C to quit)\n")
			while True:
				try:
					message = input("> ")
					if not message: 
						break
					sock.sendall(message.encode("utf-8"))
					response = sock.recv(4096)
					if response:
						print(f"Server echo: {response.decode('utf-8')}")
				except (EOFError, KeyboardInterrupt):
					break
	except ConnectionRefusedError:
		print("[-] Connection refused. Is the server running?")
	except socket.timeout:
		print("[-] Connection timeout.")
	except Exception as e:
		print(f"[-] Error: {e}")
	finally:
		print("\nClient shutting down.")
		sys.exit(0)
if __name__ == "__main__":
	start_client()

# ==============================================================
# code for Lab report 2: Implement and establish Echo Socket Client-Server Communication in Python
# server code:
import socket
import threading
import datetime
HOST = "0.0.0.0"
PORT = 1005
def handle_client(conn: socket.socket, addr):
	print(f"[+] {datetime.datetime.now().strftime('%H:%M:%S')} | New connection from {addr}")
	try:
		while True:
			data = conn.recv(4096)
			if not data:
				print(f"[-] {addr} disconnected.")
				break
			message = data.decode("utf-8")
			print(f"Received from {addr}: {message}")
			# Echo the message back
			conn.sendall(data)
			print(f"Echoed back to {addr}\n")
	except Exception as e:
		print(f"[!] Error with {addr}: {e}")
	finally:
		conn.close()
# Server startup
print(f" ECHO SERVER STARTING")
print(f" Listening on {HOST} with port {PORT}")
print("="*60)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
	server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_sock.bind((HOST, PORT))
	server_sock.listen(5)
	print("Server is up and waiting for clients...\n")
	while True:
		conn, addr = server_sock.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.daemon = True
		thread.start()
# client code:
import socket
HOST = "127.0.0.1" 
PORT = 1005
print("ECHO CLIENT")
print(f"Connecting to {HOST}in the port {PORT}...\n")
try:
	with socket.create_connection((HOST, PORT), timeout=10) as sock:
		print("[+] Successfully connected to Echo Server!\n")
		print("Start typing messages (type 'quit' or press Enter twice to exit)\n")
		while True:
			message = input("You → ")
			if message.lower() == "quit" or message == "":
				print("Goodbye!")
				break
			sock.sendall(message.encode("utf-8"))
			response = sock.recv(4096)
			print(f"Server Echo → {response.decode('utf-8')}\n")
except ConnectionRefusedError:
	print("[-] Connection refused! Is the Echo Server running?")
except socket.timeout:
	print("[-] Connection timed out.")
except KeyboardInterrupt:
	print("\nClient terminated by user.")
finally:
	print("Client closed.")

# ==============================================================
# code for Lab report 3:
# server code:
import socket
import threading
import datetime
HOST = "0.0.0.0"
PORT = 1005
def handle_client(conn: socket.socket, addr):
	print(
		f"[+] {datetime.datetime.now().strftime('%H:%M:%S')} | New connection from {addr}")
	try:
		while True:
			data = conn.recv(4096)
			if not data:
				print(f"[-] {addr} disconnected.")
				break
			message = data.decode("utf-8")
			print(f" Received from {addr}: {message}")
			conn.sendall(data)
			print(f" Echoed back to {addr}\n")
	except Exception as e:
		print(f"[!] Error with {addr}: {e}")
	finally:
		conn.close()
print(f" ECHO SERVER STARTING")
print(f" Listening on {HOST} with port {PORT}")
print("="*60)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
	server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_sock.bind((HOST, PORT))
	server_sock.listen(5)
	print("Server is up and waiting for clients...\n")
	while True:
		conn, addr = server_sock.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.daemon = True
		thread.start()
          
# client code:
import socket
HOST = "127.0.0.1"
PORT = 1005
print("ECHO CLIENT")
print(f"Connecting to {HOST} in port {PORT}...\n")
try:
    with socket.create_connection((HOST, PORT), timeout=10) as sock:
        print("[+] Successfully connected to Echo Server!\n")
        print("Start typing messages (type 'quit' or press Enter twice to exit)\n")
        while True:
            message = input("You → ")
            if message.lower() == "quit" or message == "":
                print("Goodbye!")
                break
            sock.sendall(message.encode("utf-8"))
            response = sock.recv(4096)
            print(f"Server Echo → {response.decode('utf-8')}\n")
except ConnectionRefusedError:
    print("[-] Connection refused! Is the Echo Server running?")
except socket.timeout:
    print("[-] Connection timed out.")
except KeyboardInterrupt:
    print("\nClient terminated by user.")
finally:
    print("Client closed.")

# ===================================================================
# code for lab report 4:  Implement and establish HTTP Server Responds with a Webpage in Python
# server code:
import socket

HOST = "0.0.0.0"
PORT = 1005

WELCOME_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome - Joy SD</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .container {
            text-align: center;
            padding: 60px 50px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            max-width: 600px;
            animation: fadeIn 1.5s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .wave { font-size: 3em; animation: wave 1.5s infinite; display: inline-block; }
        @keyframes wave {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(20deg); }
            50% { transform: rotate(-10deg); }
            75% { transform: rotate(15deg); }
        }
        .greeting {
            font-size: 1.4em;
            color: #aaa;
            margin-top: 15px;
            letter-spacing: 3px;
            text-transform: uppercase;
        }
        .name {
            font-size: 3.5em;
            font-weight: 800;
            background: linear-gradient(90deg, #f7971e, #ffd200, #f7971e);
            background-size: 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
            margin: 15px 0;
        }
        @keyframes shimmer {
            0% { background-position: -200% center; }
            100% { background-position: 200% center; }
        }
        .tagline {
            font-size: 1.1em;
            color: #ccc;
            margin-top: 10px;
            line-height: 1.8;
        }
        .divider {
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, #f7971e, #ffd200);
            margin: 25px auto;
            border-radius: 2px;
        }
        .info-box {
            margin-top: 25px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .info-box p {
            color: #999;
            font-size: 0.95em;
            line-height: 1.8;
        }
        .info-box span { color: #ffd200; font-weight: 600; }
        .footer {
            margin-top: 30px;
            color: #555;
            font-size: 0.85em;
        }
        form {
            margin-top: 25px;
            display: flex;
            gap: 10px;
            justify-content: center;
        }
        input[type="text"] {
            padding: 12px 20px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.15);
            background: rgba(255,255,255,0.08);
            color: #fff;
            font-size: 1em;
            outline: none;
            width: 250px;
        }
        input[type="text"]:focus { border-color: #ffd200; }
        input[type="submit"] {
            padding: 12px 25px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(90deg, #f7971e, #ffd200);
            color: #1a1a2e;
            font-weight: 700;
            font-size: 1em;
            cursor: pointer;
            transition: transform 0.2s;
        }
        input[type="submit"]:hover { transform: scale(1.05); }
    </style>
</head>
<body>
    <div class="container">
        <div class="wave">&#128075;</div>
        <p class="greeting">Welcome to the page of</p>
        <h1 class="name">Joy SD</h1>
        <div class="divider"></div>
        <p class="tagline">
            Hello there! Glad you stopped by.<br>
            This server is up and running, built with Python sockets.
        </p>
        <div class="info-box">
            <p>
                <span>Lab 4:</span> HTTP Server Responds with a Webpage<br>
                <span>Course:</span> 7th Semester - Computer Networks Lab<br>
                <span>Server:</span> Python Socket Programming
            </p>
        </div>
        <form method="POST">
            <input type="text" name="message" placeholder="Say something..." required>
            <input type="submit" value="Send">
        </form>
        <p class="footer">Powered by Python &bull; Made with care by Joy SD</p>
    </div>
</body>
</html>"""

RESPONSE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Response - Joy SD</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            display: flex; justify-content: center; align-items: center;
        }
        .container {
            text-align: center; padding: 50px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 24px; backdrop-filter: blur(10px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            animation: fadeIn 1s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .check { font-size: 3em; color: #00ff88; }
        h1 { color: #ffd200; margin: 15px 0; font-size: 1.8em; }
        .msg {
            font-size: 1.3em; color: #fff;
            background: rgba(255,255,255,0.08); padding: 15px 30px;
            border-radius: 12px; margin: 20px 0; display: inline-block;
        }
        a {
            display: inline-block; margin-top: 20px; padding: 12px 30px;
            background: linear-gradient(90deg, #f7971e, #ffd200);
            color: #1a1a2e; text-decoration: none; border-radius: 12px;
            font-weight: 700; transition: transform 0.2s;
        }
        a:hover { transform: scale(1.05); }
    </style>
</head>
<body>
    <div class="container">
        <div class="check">&#10004;</div>
        <h1>Message Received!</h1>
        <div class="msg">"{message}"</div><br>
        <a href="/">&#8592; Back to Home</a>
    </div>
</body>
</html>"""

def handle_request(client_socket):
    request = client_socket.recv(4096).decode("utf-8")
    print(f"Request received:\n{request[:200]}...")

    if "POST" in request:
        body = request.split("\r\n\r\n")[1] if "\r\n\r\n" in request else ""
        from urllib.parse import unquote_plus
        message = unquote_plus(body.split("=")[1]) if "=" in body else "No message"
        response_body = RESPONSE_TEMPLATE.replace("{message}", message)
    else:
        response_body = WELCOME_PAGE

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        + response_body
    )
    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()
    print("Response sent.\n")

# Start server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(5)
    print("=" * 50)
    print("   Joy SD's HTTP Server")
    print("=" * 50)
    print(f"   Running on http://127.0.0.1:{PORT}")
    print("   Press Ctrl+C to stop")
    print("=" * 50)
    while True:
        client_sock, addr = server_sock.accept()
        print(f"Connection from {addr}")
        handle_request(client_sock)
# ===================================================================

# code for lab report 5: Create a Simple HTTP server in python
# server: 
import http.server
import socketserver

PORT = 1005

class joy_HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request from {self.client_address}")
        super().do_GET()
def joy_run_server():
    with socketserver.TCPServer(("", PORT), joy_HTTPRequestHandler) as httpd:
        print(f"Serving HTTP on port {PORT}...")
        print(f"Open your browser and visit: http://localhost:{PORT}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by Joy.")
            httpd.server_close()

if __name__ == "__main__":
    joy_run_server()

# ===================================================================
# code for lab report 6: Create a HTTP server only as localhost serving in python
# server code:
import http.server
import socketserver

HOST = "127.0.0.1" 
PORT = 3063

class joy_LocalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"[Log] joy_LocalHandler received request from: {self.client_address}")
        super().do_GET()

def joy_run_localhost_server():
    with socketserver.TCPServer((HOST, PORT), joy_LocalHandler) as httpd:
        print(f"Server started by Joy.")
        print(f"Serving exclusively on: http://{HOST}:{PORT}")
        print(f"External access (LAN) is disabled.")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by Joy.")
            httpd.server_close()

if __name__ == "__main__":
    joy_run_localhost_server()
# ===================================================================
# code for lab report 7: Test html code and a web page with previous 5 and 6 no. HTTP server
# server code:
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


# ===================================================================
# code for lab report 8:  Create a Simple DNS Server
# server code:
import socket

HOST = "0.0.0.0"
PORT = 9953  # Custom DNS Port

# Simple DNS database
dns_records = {
    "google.com": "142.250.193.14",
    "facebook.com": "157.240.22.35",
    "youtube.com": "142.250.190.14",
    "localhost": "127.0.0.1"
}

# Get local network IP (for devices on the same Wi-Fi/LAN)
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Could not detect"

local_ip = get_local_ip()

print("SIMPLE DNS SERVER STARTING...")
print(f"Listening on {HOST}:{PORT}")
print("=" * 50)
print(f"Your Local/Network IP : {local_ip}")
print(f"Other devices should connect to : {local_ip}:{PORT}")
print(f"On this machine, use            : 127.0.0.1:{PORT}")
print("=" * 50)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    
    while True:
        data, addr = server.recvfrom(1024)
        domain = data.decode("utf-8").strip().lower()
        
        print(f"Query from {addr}: {domain}")
        
        ip = dns_records.get(domain, "Domain not found")
        
        server.sendto(ip.encode("utf-8"), addr)
        print(f"Response sent: {ip}\n")
        
# client code:

import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9953

print("SIMPLE DNS CLIENT")
print(f"Connecting to DNS Server at {SERVER_HOST}:{SERVER_PORT}\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    
    while True:
        domain = input("Enter domain name (type 'quit' to exit): ").lower()
        
        if domain == "quit":
            print("Client exiting...")
            break
        
        client.sendto(domain.encode("utf-8"), (SERVER_HOST, SERVER_PORT))
        
        response, _ = client.recvfrom(1024)
        print(f"IP Address: {response.decode('utf-8')}\n")
# ==============================================================
# lab report 9 : create a server connecting a different device 

#  same as the previous just connect the proper port in same network for separate device
# ==============================================================
# lab report 10: Access the Site with local DNS server ---> csebatcheight(your_reg_number).com

# server code:


import socket

HOST = "0.0.0.0"
DNS_PORT = 9953  # Custom DNS Port

# ---------- Get Local Network IP ----------
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

# ---------- DNS Records Database ----------
# Maps custom domain names to IP addresses
dns_records = {
    "csebatcheight1005.com": LOCAL_IP,       # Your lab domain -> points to this machine
    "www.csebatcheight1005.com": LOCAL_IP,   # With www prefix
    "google.com": "142.250.193.14",
    "facebook.com": "157.240.22.35",
    "youtube.com": "142.250.190.14",
    "localhost": "127.0.0.1",
}

# ---------- Start DNS Server ----------
print("=" * 60)
print("   Lab 10: LOCAL DNS SERVER")
print("=" * 60)
print(f"   Server IP Address   : {LOCAL_IP}")
print(f"   DNS Port            : {DNS_PORT}")
print(f"   Web Server Port     : 8080")
print("-" * 60)
print("   DNS Records:")
for domain, ip in dns_records.items():
    print(f"     {domain:40s} -> {ip}")
print("-" * 60)
print(f"   [Client] Set SERVER_HOST = \"{LOCAL_IP}\"")
print(f"   [Browser] After DNS lookup, visit http://{LOCAL_IP}:8080")
print("=" * 60)
print("\n   Waiting for DNS queries...\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, DNS_PORT))

    while True:
        data, addr = server.recvfrom(1024)
        domain = data.decode("utf-8").strip().lower()

        print(f"   [QUERY]    From {addr[0]}:{addr[1]}  ->  {domain}")

        ip = dns_records.get(domain, "ERROR: Domain not found")

        server.sendto(ip.encode("utf-8"), addr)
        print(f"   [RESPONSE] {domain}  ->  {ip}\n")


# webserver code:


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

# client code:


import socket

SERVER_HOST = "127.0.0.1"   # Change to server's IP if on a different device
SERVER_PORT = 9953

print("=" * 60)
print("   Lab 10: LOCAL DNS CLIENT")
print("=" * 60)
print(f"   DNS Server : {SERVER_HOST}:{SERVER_PORT}")
print("=" * 60)
print("   Type a domain name to resolve (e.g., csebatcheight1005.com)")
print("   Type 'quit' to exit\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:

    while True:
        domain = input("   Enter domain: ").strip().lower()

        if domain == "quit":
            print("\n   Client exiting...")
            break

        if not domain:
            continue

        client.sendto(domain.encode("utf-8"), (SERVER_HOST, SERVER_PORT))

        response, _ = client.recvfrom(1024)
        resolved_ip = response.decode("utf-8")

        print(f"   Resolved IP: {resolved_ip}")

        if not resolved_ip.startswith("ERROR"):
            print(f"   Access site: http://{resolved_ip}:8080")
        print()


