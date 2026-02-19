import socket
import urllib.request
from dnslib import DNSRecord, QTYPE

# Configuration
DNS_SERVER = ("127.0.0.1", 5053)
HTTP_PORT = 3063
DOMAIN_TO_TEST = "csebatcheight.com"

def Faysal_test_setup():
    print(f"--- Testing Faysal's Lab 10 Setup ---")
    
    # 1. DNS QUERY
    print(f"\n[Step 1] Querying DNS Server for {DOMAIN_TO_TEST}...")
    try:
        # Create DNS Query Packet using dnslib
        q = DNSRecord.question(DOMAIN_TO_TEST)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.sendto(q.pack(), DNS_SERVER)
        
        # Get Response
        data, _ = sock.recvfrom(512)
        d = DNSRecord.parse(data)
        
        # Extract IP
        resolved_ip = str(d.rr[0].rdata)
        print(f" -> Success! {DOMAIN_TO_TEST} resolved to {resolved_ip}")
        
    except Exception as e:
        print(f" -> DNS Failed: {e}")
        return

    # 2. HTTP REQUEST
    print(f"\n[Step 2] Fetching Web Page from {resolved_ip}:{HTTP_PORT}...")
    try:
        url = f"http://{resolved_ip}:{HTTP_PORT}/"
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(" -> HTTP Success! Content received:\n")
            print(content)
            
    except Exception as e:
        print(f" -> HTTP Failed: {e}")

if __name__ == "__main__":
    Faysal_test_setup()