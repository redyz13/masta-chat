import socket
import subprocess

class Server():
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        # Test