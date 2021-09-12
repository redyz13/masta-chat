import ServerMain
import ClientMain

if __name__ == '__main__':
    select = int(input("\nSelezionare un opzione\n\n1. Crea chat\n2. Partecipa a chat\n0. Esci\n\nSelezione: "))

    if select == 1:
        ServerMain.dashboard()
    elif select == 2:
        ClientMain.dashboard()
    else:
        exit()