import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
HOST = '127.0.0.1'  
PORT = 23456
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Receive data from the client and change it to upper-case send it back
data = client_socket.recv(1024)
print(f"Received: {data.decode('utf-8')}")
upper_data = data.upper()
client_socket.send(upper_data)  # send the data to the client

# Close the client socket
client_socket.close()
