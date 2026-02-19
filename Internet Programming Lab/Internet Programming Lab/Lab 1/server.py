import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print("Client connected:", addr)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"Received from {addr}: {message}")

            # Normal response (NOT echo)
            response = "Message received"
            conn.send(response.encode())

    except socket.error as e:
        print("Client error:", e)

    finally:
        conn.close()
        print("Client disconnected:", addr)

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Multi-Client Server running...")

    while True:
        conn, addr = server_socket.accept()

        # New thread for each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

except socket.error as e:
    print("Server error:", e)

finally:
    server_socket.close()

