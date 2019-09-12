import socket, threading, json
from datetime import datetime

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket,coordinate_list):
        #add connection
        threading.Thread.__init__(self)
        self.conn = clientsocket
        self.data = coordinate_list
        print ("\nNew connection added: ", clientAddress)
        
    def run(self):
        #send data
        dateTimeObj = datetime.now()
        print(dateTimeObj)
        print ("Connection from : ", clientAddress)
        answer = 'try again'
        while(answer == 'try again'):
            self.conn.sendall(bytes(str(len(','.join(self.data))), 'utf-8'))
            self.conn.sendall(bytes(','.join(self.data), 'utf-8'))
            answer = self.conn.recv(100).decode("utf-8")
        print ("Client at ", clientAddress , " disconnected...")

#read coordinates
with open('coordinates.json') as f:
    coordinate_list = json.load(f)


LOCALHOST = "127.0.0.1"
PORT = 9991

#start Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")

#wait for clients
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock,coordinate_list)
    newthread.start()
