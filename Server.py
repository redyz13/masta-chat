import socket
from subprocess import TimeoutExpired

class Server():
    def __init__(self, port):
        self.__serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)
        self.__port = port
        self.__clientSocket = None

    def acceptClient(self):
        self.__serverSocket.bind((socket.gethostname(), self.__port)) # Bind to hostname and port
        self.__serverSocket.listen(0) # Connection queue before refusing
        
        print("\n[Connessione Avviata]\tIn attesa di un client...")

        self.__serverSocket.settimeout(60)

        try:
            self.__clientSocket, address = self.__serverSocket.accept()
            print(f"\n[Connessione Effettuata]\tClient: {address} connesso")
        except socket.timeout:
            print("\n[Tempo di attesa scaduto, server arrestato]\n")
            exit()

    def sendData(self, x):
        x = str(x)
        self.__clientSocket.send(x.encode())

    def receiveData(self):
        return self.__clientSocket.recv(1024).decode("utf-8")