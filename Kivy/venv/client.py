import socket
import pickle
import json

class Client:
    def __init__(self):
        self.soc =socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    def req(self,input):
        self.soc.connect((socket.gethostname(), 1234))
        self.soc.send(bytes(input,"utf-8"))
        return self.soc.recv(1024).decode("utf-8")


