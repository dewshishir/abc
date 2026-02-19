import socket

HOST = "127.0.0.1"
PORT = 4000

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and port
server_socket.bind((HOST, PORT))

# Listen for connection
server_socket.listen(1)

print(f"Echo Server running at {HOST}:{PORT}")

conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Received:", data)

    # Echo back
    conn.send(data.encode())

conn.close()
server_socket.close()
