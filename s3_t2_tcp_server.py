import socket

SERVER_IP = '0.0.0.0' # Listen on all available interfaces
SERVER_PORT = 9999    # A high, non-privileged port

def run_server():
    # AF_INET for IPv4, SOCK_STREAM for TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5) # Set maximum backlog of connections

    print(f"[*] Listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Accept a connection when received
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # Receive data (up to 1024 bytes)
        data = client_socket.recv(1024)
        print(f"[*] Received: {data.decode('utf-8')}")

        # Send a simple response back
        client_socket.send(b"ACK: Message received successfully!\n")
        client_socket.close()

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n[*] Server shutting down...")
    except Exception as e:
        print(f"[ERROR] Server failed: {e}")
