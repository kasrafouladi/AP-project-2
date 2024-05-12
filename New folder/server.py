import socket

def start_echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Echo server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connected to {client_address}")
            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    client_socket.sendall(data)  # Echo back the received data
            print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    HOST = "0.0.0.0"  # Use your server's IP address or hostname
    PORT = 8000  # Choose an available port
    start_echo_server(HOST, PORT)
