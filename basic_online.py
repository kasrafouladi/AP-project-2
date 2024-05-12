import socket
import json

def check_internet_connection():
    try:
        # Create a socket and connect to a well-known external server (e.g., Google's DNS server)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('8.8.8.8', 53))  # Google's DNS server IP and port 53
        s.close()
        return True  # Connection successful, internet is available
    except socket.error:
        return False  # Connection failed, no internet access

def get_public_ip():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the IP address of the ipify.org server
    s.connect(('api64.ipify.org', 80))
    # Send an HTTP GET request
    s.send(b'GET /?format=json HTTP/1.1\r\nHost: api64.ipify.org\r\n\r\n')
    # Receive the response
    response = s.recv(1024).decode('utf-8')
    # Close the socket
    s.close()
    # Parse the JSON response
    data = json.loads(response.split('\r\n\r\n')[1])
    print(data)
    print("*****")
    return data['ip']

print(get_public_ip())