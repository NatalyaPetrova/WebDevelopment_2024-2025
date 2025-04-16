import socket

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, server")
    data = s.recv(1024)
    print(f"[CLIENT] Ответ от сервера: {data.decode()}")

