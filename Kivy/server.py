import socket
from scraper import Scrap
import pickle
import pickle
import json

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    msg = clientsocket.recv(1024)
    nome= msg.decode("utf-8")
    sc= Scrap(nome)
    clientsocket.send(bytes(sc.info(),"utf-8"))
    clientsocket.close()

