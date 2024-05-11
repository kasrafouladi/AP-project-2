import socket

def send_message_to_server(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    HOST = "0.0.0.0"  # Use your server's IP address or hostname
    PORT = 80  # Use the same port as the server

    user_input = input("Enter a message to send to the server: ")
    send_message_to_server(HOST, PORT, user_input)