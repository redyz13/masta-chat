from .server import Server

def run():
    while True:
        pass
    
def connection():
    server = Server(7000) # Server port
    server.acceptClient()

    print("\n[Server in esecuzione]\n")

    run()

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Avvia Connessione\n0. Esci\n\nSelezione: "))

    connection() if select == 1 else exit()