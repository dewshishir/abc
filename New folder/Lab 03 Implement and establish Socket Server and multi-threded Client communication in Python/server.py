import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"[{address}] {message}")

            response = f"Server received: {message}"
            client_socket.send(response.encode())

        except:
            break

    print(f"[DISCONNECTED] {address}")
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[STARTED] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()

        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
