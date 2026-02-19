import socket

HOST = "127.0.0.1"
PORT = 4000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to Echo Server")

while True:
    message = input("Enter message (type 'exit' to quit): ")

    if message.lower() == "exit":
        break

    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Echo from server:", response)

client_socket.close()
