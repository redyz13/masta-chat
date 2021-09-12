import server.s_dashboard as server
import client.c_dashboard as client

if __name__ == '__main__':
    select = int(input("\nSelezionare un opzione\n\n1. Crea chat\n2. Partecipa a chat\n0. Esci\n\nSelezione: "))

    server.dashboard() if select == 1 else\
        (client.dashboard() if select == 2 else\
            exit())