# server.py
import socket
import threading
import random

def get_forecast():
    forecasts = [
        "Sunny and warm",
        "Cloudy with light rain",
        "Thunderstorms expected",
        "Snow showers",
        "Mild with some clouds"
    ]
    return random.choice(forecasts)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        request = data.decode('utf-8')
        print(f"[REQUEST] {request} from {addr}")
        if request.lower() == "forecast":
            response = get_forecast()
            conn.sendall(response.encode('utf-8'))
        else:
            conn.sendall(b"Unknown command")
    conn.close()

def main():
    HOST = '127.0.0.1'
    PORT = 65432
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] MCP Weather Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()