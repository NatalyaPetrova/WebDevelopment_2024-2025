import socket
import math

HOST = 'localhost'
PORT = 65432

def solve_quadratic(a, b, c):
    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # два действительных корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Два корня: x1 = {root1:.2f}, x2 = {root2:.2f}"
    elif discriminant == 0:
        # один корень
        root = -b / (2 * a)
        return f"Один корень: x = {root:.2f}"
    else:
        # нет действительных корней
        return "Нет действительных корней"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Ожидаем подключение на {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Подключен клиент: {addr}")
        data = conn.recv(1024).decode()
        print(f"[SERVER] Получены данные: {data}")

        # Разбираем коэффициенты a, b, c
        try:
            a_str, b_str, c_str = data.strip().split()
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)

            # Решаем квадратное уравнение
            response = solve_quadratic(a, b, c)
        except Exception as e:
            response = f"Ошибка обработки данных: {e}"

        # Отправляем результат обратно клиенту
        conn.sendall(response.encode())

