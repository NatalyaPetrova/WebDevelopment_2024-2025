import socket

HOST = 'localhost'
PORT = 65432


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Запрашиваем у пользователя коэффициенты
        print("Введите коэффициенты квадратного уравнения ax^2 + bx + c = 0")
        a = input("Введите коэффициент a: ")
        b = input("Введите коэффициент b: ")
        c = input("Введите коэффициент c: ")

        # Отправляем коэффициенты серверу
        coefficients = f"{a} {b} {c}"
        s.sendall(coefficients.encode())

        # Получаем ответ от сервера
        data = s.recv(1024).decode()
        print("Результат решения:", data)


if __name__ == "__main__":
    start_client()


