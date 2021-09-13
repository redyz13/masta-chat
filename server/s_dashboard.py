from .server import Server
from threading import *

def send_thread(server, server_username):
    while True:
        message_sent = input(f"\n[{server_username}]: ")
        server.send_data(message_sent)

def receive_thread(server, client_username):
    while True:
        message_received = server.receive_data()
        print(f"[{client_username}]: {message_received}")

def run(server):
    server_username = input("Inserire il proprio username: ")
    print("")
    
    client_username = server.receive_data()
    server.send_data(server_username)
    
    thread1 = Thread(target = lambda: send_thread(server, server_username))
    thread2= Thread(target = lambda: receive_thread(server, client_username))

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