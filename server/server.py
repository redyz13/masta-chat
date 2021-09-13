import socket

class Server():
    def __init__(self, port):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (LAN, Internet) SOCK_STREAM (TCP)
        self.__port = port
        self.__client_socket = None
        self.__server_socket.settimeout(60) # Connection timeout (seconds)

    def accept_client(self):
        self.__server_socket.bind(("", self.__port)) # Bind to hostname and port
        self.__server_socket.listen(0) # Connection queue before refusing
        
        print("\n[Connessione Avviata]\tIn attesa di un client...")

        try:
            self.__client_socket, address = self.__server_socket.accept()
            print(f"\n[Connessione Effettuata]\tClient: {address} connesso")
        except socket.timeout:
            print("\n[Tempo di attesa scaduto, server arrestato]\n")
            exit()

    def send_data(self, x):
        x = str(x)
        self.__client_socket.send(x.encode())

    def receive_data(self):
        return self.__client_socket.recv(1024).decode("utf-8")

    def get_socket(self):
        return self.__client_socket 