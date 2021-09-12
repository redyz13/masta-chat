from Server import Server

if __name__ == '__main__':
    server = Server("localhost", 7000)
    print(server.getIp())
    