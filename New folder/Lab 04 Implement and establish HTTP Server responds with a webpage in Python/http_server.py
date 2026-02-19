import socket
import os

HOST = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server running at http://{HOST}:{PORT}")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "index.html")

while True:
    client_socket, address = server_socket.accept()
    print("Connection from:", address)

    request = client_socket.recv(1024).decode()
    print("Request received:\n", request)

    with open(file_path, "r") as file:
        html_content = file.read()

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n\r\n"
    response += html_content

    client_socket.send(response.encode())
    client_socket.close()
