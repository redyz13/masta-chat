import socket

class Client():
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)

    def connect(self):
        self.__client_socket.settimeout(10) # Connection timeout (seconds)
        self.__client_socket.connect((self.__ip, self.__port))


    def send_data(self, x):
        x = str(x)
        self.__client_socket.send(x.encode())

    def receive_data(self):
        return self.__client_socket.recv(1024).decode("utf-8")