"""
 Implements a simple socket client

"""

import socket


# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send message
while True:
    msg = input("> ")
    client_socket.sendall(msg.encode())

    if(msg == 'exit'):
        break

    msg = client_socket.recv(1024).decode()
    print(SERVER_HOST+" > ", msg)
# Close socket
client_socket.close()
