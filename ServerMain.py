from Server import Server

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

    if select == 1:
        connection()
    else:
        exit()

if __name__ == '__main__':
    dashboard()
    