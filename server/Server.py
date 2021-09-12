import socket
import subprocess

class Server():
    def __init__(self, port):
        __server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)
        self.__port = port

    def acceptClient(self):
        self.__server.bind(socket.gethostname(), 7000) # Bind to hostname and port
        self.__server.listen(0) # Connection queue before refusing
