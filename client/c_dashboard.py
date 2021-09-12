from .client import Client

def run():
    pass

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

    run()

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Connetti\n0. Esci\n\nSelezione: "))

    connect() if select == 1 else exit()