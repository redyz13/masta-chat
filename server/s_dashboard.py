from .server import Server
from threading import *

def thread_send(server, server_username):
    while True:
        message_sent = input(f"[{server_username}]: ")

        try:
            server.send_data(message_sent)
        except BrokenPipeError:
            print("\n[Connessione con il client terminata]")
            exit()

def thread_receive(server, client_username):
    while True:
        message_received = server.receive_data()
        print(message_received)

        if message_received != "":
            print(f"[{client_username}]: {message_received}") 

def run(server):
    server_username = input("Inserire il proprio username: ")
    print("")
    
    client_username = server.receive_data()
    server.send_data(server_username)
    
    thread1 = Thread(target = lambda: thread_send(server, server_username))
    thread2= Thread(target = lambda: thread_receive(server, client_username))

    thread1.start()
    thread2.start()
    
def connection():
    server = Server(7000) # Server port
    server.accept_client()

    print("\n[Server in esecuzione]\n")

    run(server)

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Avvia Connessione\n0. Esci\n\nSelezione: "))

    connection() if select == 1 else exit()