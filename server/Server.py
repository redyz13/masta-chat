import socket
import subprocess

class Server():
    def __init__(self, port):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)
        self.__port = port
        self.__clientSocket = None

    def acceptClient(self):
        self.__server.bind((socket.gethostname(), self.__port)) # Bind to hostname and port
        self.__server.listen(0) # Connection queue before refusing
        
        print("\n[Connessione Avviata]\tIn attesa di un client...")

        self.__clientSocket = self.__server.accept()

        print(f"\n[Connessione Effettuata]\tClient: {self.__clientSocket.gethostname()} connesso")

    def sendData(self, x):
        x = str(x)
        self.__clientSocket.send(x.encode())

    def receiveData(self):
        return self.__clientSocket.recv(1024)