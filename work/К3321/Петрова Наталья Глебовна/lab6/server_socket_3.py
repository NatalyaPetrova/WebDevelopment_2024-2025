import socket
HOST = 'localhost'
PORT = 65432
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # Привязываем сокет к адресу и порту
        s.listen(1)  # Сервер будет ожидать одно подключение
        print(f"[SERVER] Ожидаем подключения на {HOST}:{PORT}...")

        conn, addr = s.accept()  # Принимаем подключение от клиента
        with conn:
            print(f"[SERVER] Подключен клиент: {addr}")

            # Подгружаем HTML файл (main.html)
            try:
                with open('main.html', 'r', encoding='utf-8') as f:
                    html_content = f.read()

                # Отправляем HTML-страницу клиенту
                conn.sendall(html_content.encode())
            except FileNotFoundError:
                # Если файл не найден, отправляем ошибку 404
                response = "404 - Страница не найдена"
                conn.sendall(response.encode())


if __name__ == "__main__":
    start_server()


