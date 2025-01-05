import socket
import random
import time
from datetime import datetime

def startclient(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
        clientsocket.connect((host, port))
        print("Подключено к серверу")

        while True:
            sensor_value = random.randint(0, 100)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"{current_time}, {sensor_value}"

            clientsocket.sendall(message.encode('utf-8'))
            print(f"Отправлено: {message}")

            time.sleep(60)

if __name__ == "__main__":
    startclient()