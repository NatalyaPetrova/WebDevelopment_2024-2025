import socket
import webbrowser
import os

HOST = 'localhost'
PORT = 65432

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Подключаемся к серверу

        # Получаем ответ от сервера (HTML-контент)
        data = s.recv(1024).decode()
        print("Результат получения страницы:")

        # Сохраняем полученный HTML-контент в файл
        with open('received_page.html', 'w', encoding='utf-8') as file:
            file.write(data)

        # Открываем файл в браузере
        if "404" not in data:
            webbrowser.open('file://' + os.path.realpath('received_page.html'))
        else:
            print(data)  # В случае ошибки выводим сообщение


if __name__ == "__main__":
    start_client()




