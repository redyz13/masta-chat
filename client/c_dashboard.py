from subprocess import TimeoutExpired
from .client import Client
from threading import *
import socket

def thread_send(client, client_username):
    while True:
        message_sent = input(f"[{client_username}]: ")

        try:
            client.send_data(message_sent)
        except BrokenPipeError:
            print("\n[Connessione con il server terminata]")
            exit()

def thread_receive(client, server_username):
    #TIMEOUT = 3

    while True:
        #client.get_socket().settimeout(TIMEOUT)

        #try:
        message_received = client.receive_data()
        """except socket.timeout:
            print(f"\n\n[Nessun input ricevuto negli ultimi {TIMEOUT} secondi, connessione terminata]")
            exit()"""
        
        if message_received != "":
            print(f"[{server_username}]: {message_received}")

def run(client):
    client_username = input("Inserire il proprio username: ")
    print("")

    client.send_data(client_username)
    server_username = client.receive_data()

    thread1 = Thread(target = lambda: thread_send(client, client_username))
    thread2= Thread(target = lambda: thread_receive(client, server_username))

    thread1.start()
    thread2.start()

def connect():
    ip = input("\nInserire l'indirizzo IP del server: ")
    port = int(input("Inserire la porta del server: "))

    client = Client(ip, port) # Server port

    try:
        client.connect()
        print("\n[Connessione effettuata]\n")
    except ConnectionRefusedError:
        print("\n[Connessione rifiutata]") 
        dashboard()
    except socket.timeout:
        print("\n[Errore di connessione]") 
        dashboard()

    run(client)

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Connetti\n0. Esci\n\nSelezione: "))

    connect() if select == 1 else exit()