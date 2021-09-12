import socket

class Client():
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)

    def connect(self):
        self.__clientSocket.connect((self.__ip, self.__port))

    def sendData(self, x):
        x = str(x)
        self.__clientSocket.send(x.encode())

    def receiveData(self):
        return self.__clientSocket.recv(1024).decode("utf-8")