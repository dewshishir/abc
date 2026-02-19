import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")

while True:
    message = input("Enter message (type 'exit' to quit): ")

    if message.lower() == "exit":
        break

    client.send(message.encode())
    response = client.recv(1024).decode()
    print("Server:", response)

client.close()
