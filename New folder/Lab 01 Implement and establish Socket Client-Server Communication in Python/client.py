import socket

HOST = "127.0.0.1"
PORT = 3000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

# Send message
message = "Hello Server"
client_socket.send(message.encode())

# Receive reply
response = client_socket.recv(1024).decode()
print("Server replied:", response)

client_socket.close()
