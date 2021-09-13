from .server import Server

def run(server):
    server_username = input("Inserire il proprio username: ")
    print("")
    
    client_username = server.receive_data()
    server.send_data(server_username)

    while True:
        message_received = server.receive_data()
        print(f"[{client_username}]: {message_received}")

        message_sent = input(f"\n[{server_username}]: ")
        server.send_data(message_sent)
    
def connection():
    server = Server(7000) # Server port
    server.accept_client()

    print("\n[Server in esecuzione]\n")

    run(server)

def dashboard():
    select = int(input("\nSelezionare un opzione\n\n1. Avvia Connessione\n0. Esci\n\nSelezione: "))

    connection() if select == 1 else exit()