import socket
import threading
from pystyle import Colors, Colorate

def start_honeypot():
    HOST = '0.0.0.0'
    PORT = 22

    def handle_client(conn, addr):
        print(Colorate.Horizontal(Colors.red_to_yellow ,f"Подключение от {addr}"))
        with conn:
            conn.sendall(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(Colorate.Horizontal(Colors.red_to_yellow ,f"Получены данные от {addr}: {data}"))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(Colorate.Horizontal(Colors.red_to_yellow , f"Прослушивание порта {PORT}..."))
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
