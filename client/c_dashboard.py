from .client import Client
from threading import *

def send_thread(client, client_username):
    while True:
        message_sent = input(f"\n[{client_username}]: ")
        client.send_data(message_sent)

def receive_thread(client, server_username):
    while True:
        message_received = client.receive_data()
        print(f"[{server_username}]: {message_received}")

def run(client):
    client_username = input("Inserire il proprio username: ")

    client.send_data(client_username)
    server_username = client.receive_data()

    thread1 = Thread(target = lambda: send_thread(client, client_username))
    thread2= Thread(target = lambda: receive_thread(client, server_username))

    thread1.start()
    thread2.start()

def connect():
    ip = input("\nInserire l'indirizzo IP del server: ")
    port = int(input("Inserire la porta del server: "))

    client = Client(ip, port) # Server port

    try:
        client.connect()
        print("\n[Connessione effettuata]\n")
    except Exception:
        print("\n[Errore di connessione]") 
        dashboard()  

    run(client)

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Connetti\n0. Esci\n\nSelezione: "))

    connect() if select == 1 else exit()