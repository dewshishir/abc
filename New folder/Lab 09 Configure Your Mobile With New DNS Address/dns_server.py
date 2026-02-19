import socket

# Replace with your actual IPv4
PC_IP = "192.168.0.183"

DNS_PORT = 53

def build_response(data):
    transaction_id = data[:2]
    flags = b'\x81\x80'
    questions = b'\x00\x01'
    answer_rrs = b'\x00\x01'
    authority_rrs = b'\x00\x00'
    additional_rrs = b'\x00\x00'

    dns_header = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs

    query = data[12:]
    domain_parts = []
    i = 0
    while query[i] != 0:
        length = query[i]
        domain_parts.append(query[i+1:i+1+length].decode())
        i += length + 1

    domain_name = ".".join(domain_parts)
    print("Query for:", domain_name)

    answer = b'\xc0\x0c'      # Pointer to domain name
    answer += b'\x00\x01'     # Type A
    answer += b'\x00\x01'     # Class IN
    answer += b'\x00\x00\x00\x3c'  # TTL 60 seconds
    answer += b'\x00\x04'
    answer += socket.inet_aton(PC_IP)

    return dns_header + data[12:] + answer

def start_dns():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", DNS_PORT))

    print("DNS Server Running on Port 53")
    print("Redirecting all domains to:", PC_IP)

    while True:
        data, addr = server.recvfrom(512)
        response = build_response(data)
        server.sendto(response, addr)

if __name__ == "__main__":
    start_dns()
