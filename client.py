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

#####################################
while True:
    # Send message
    msg = input("> ")
    client_socket.send(msg.encode())
    msgEco = client_socket.recv(1024).decode()
    print('Received:', msgEco)
    if msg == "exit":
        break
#####################################

# Close socket
client_socket.close()
