from Client import Client

def run():
    pass

def connect():
    ip = input("\nInserire l'indirizzo IP del server: ")
    port = int(input("Inserire la porta del server: "))

    client = Client(ip, port) # Server port

    try:
        client.connect()
        print("\n[Connessione effettuata]\n")
    except ConnectionRefusedError:
        print("\n[Errore di connessione]")
        dashboard()
    except Exception:
        print("\n[IP errato]") 
        dashboard()        

    run()

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Connetti\n0. Esci\n\nSelezione: "))

    if select == 1:
        connect()
    else:
        exit()

if __name__ == '__main__':
    dashboard()