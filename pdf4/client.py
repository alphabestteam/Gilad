import socket


def main():
    HOST = "127.0.0.1"
    PORT = 23456

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    message = "Hi my name is Gilad"

    # Send the message to the server
    client_socket.send(message.encode("utf-8"))

    # Receive and print the server's response
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode('utf-8')}")

    # Close the client socket
    client_socket.close()


if __name__ == "__main__":
    main()
