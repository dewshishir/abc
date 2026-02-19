import socket

# Custom DNS Records (Domain → IP Mapping)
DNS_TABLE = {
    "csebatcheight1002.com": "127.0.0.1",
    "google.local": "8.8.8.8",
    "test.local": "192.168.1.10"
}

HOST = "127.0.0.1"   # Run locally
PORT = 5053         # Custom DNS port (avoid 53 - requires admin)

def start_dns_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print(f"DNS Server running on {HOST}:{PORT}")
    print("Waiting for DNS queries...\n")

    while True:
        data, addr = server_socket.recvfrom(1024)
        domain = data.decode().strip()

        print(f"Received query for: {domain}")

        ip = DNS_TABLE.get(domain, "Domain not found")

        server_socket.sendto(ip.encode(), addr)
        print(f"Sent response: {ip}\n")

if __name__ == "__main__":
    start_dns_server()
