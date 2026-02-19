import socket

HOST = "127.0.0.1"
PORT = 5053   # Must match server port

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain: ")
client.sendto(domain.encode(), (HOST, PORT))

response, _ = client.recvfrom(1024)
print("IP Address:", response.decode())

client.close()
