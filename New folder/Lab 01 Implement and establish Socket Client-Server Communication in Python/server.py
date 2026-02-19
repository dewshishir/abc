import socket

HOST = "127.0.0.1"
PORT = 3000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and Port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server running at {HOST}:{PORT}")

# Accept connection
conn, addr = server_socket.accept()
print("Connected by", addr)

# Receive message from client
data = conn.recv(1024).decode()
print("Message from client:", data)

# Send reply to client
reply = "Message received successfully"
conn.send(reply.encode())

# Close connection
conn.close()
server_socket.close()
