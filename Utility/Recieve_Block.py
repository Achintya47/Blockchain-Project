import socket
import threading

def recieve_block():
    host = "0.0.0.0"  # Listen on all interfaces
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 pending connections

    print(f"Server listening on {host}:{port}")

    def handle_client(conn, addr):
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
        conn.close()

    while True:
        conn, addr = server_socket.accept()
        # Create a new thread to handle the client connection
        threading.Thread(target=handle_client, args=(conn, addr)).start()
