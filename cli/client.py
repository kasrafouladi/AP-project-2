import socket

def send_message_to_server(host, port, message):
    print('*')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print("-")
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        print("0")
        response = client_socket.recv(1024)
        print("1")
        print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    HOST = "0.0.0.0"  # Use your server's IP address or hostname
    PORT = 8000  # Use the same port as the server

    user_input = input("Enter a message to send to the server: ")
    send_message_to_server(HOST, PORT, user_input)