import socket

# domain:5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5000))
server_socket.listen()

while True:
    print("-" * 5, "Server started", "-" * 5)
    client_socket, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            responce = "Hello world\n".encode()
            client_socket.send(responce)

    print("Hello outside inner func")
    server_socket.close()
