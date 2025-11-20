import socket
import sys

# Target details for the check (using a common web port)
TARGET_HOST = "scanme.nmap.org" 
TARGET_PORT = 80 

def check_port(host, port):
    # AF_INET is address family for IPv4
    # SOCK_STREAM is socket type for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(2) # Set a 2 second timeout
        try:
            # Attempt to connect
            client.connect((host, port))
            print(f"[SUCCESS] Port {port} on {host} is OPEN (TCP SYN/ACK received).")

            # Optional: Send and receive a small amount of data
            client.sendall(b"HEAD / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n")
            response = client.recv(4096).decode(errors='ignore').split('\n')[0]
            print(f"[INFO] Server Response: {response}")

        except socket.timeout:
            print(f"[FAILURE] Port {port} on {host} TIMED OUT. Likely filtered/blocked.")
        except ConnectionRefusedError:
            print(f"[FAILURE] Port {port} on {host} REFUSED connection. Likely closed.")
        except Exception as e:
            print(f"[ERROR] Could not connect to {host}:{port}. Error: {e}")

if __name__ == "__main__":
    print(f"--- Checking {TARGET_HOST}:{TARGET_PORT} ---")
    check_port(TARGET_HOST, TARGET_PORT)
