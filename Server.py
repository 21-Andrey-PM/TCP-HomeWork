import socket

def startserver(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        serversocket.bind((host, port))
        serversocket.listen()
        print(f"Сервер запущен на {host}:{port}. Ожидание подключенияЫ")
        while True:
            conn, addr = serversocket.accept()
            with conn:
                print(f"Подключено к {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    with open('data.txt', 'a') as f:
                        f.write(data.decode('utf-8') + '\n')
                    print(f"Получено: {data.decode('utf-8')}")
if __name__ == "__main__":
    startserver()