# client.py
import socket

def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to MCP Weather Server.")
        s.sendall(b"Forecast")
        data = s.recv(1024)
        print("Weather Forecast:", data.decode('utf-8'))

if __name__ == "__main__":
    main()