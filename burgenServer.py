import socket, threading, json
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket,coordinate_list):
        threading.Thread.__init__(self)
        self.conn = clientsocket
        self.data = coordinate_list
        print ("\n New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.conn.send(bytes("Hi, This is from Server..",'utf-8'))
        self.conn.sendall(bytes(str(len(','.join(self.data))), 'utf-8'))
        self.conn.sendall(bytes(','.join(self.data), 'utf-8'))
        print ("Client at ", clientAddress , " disconnected...")


with open('coordinates.json') as f:
    coordinate_list = json.load(f)

      
LOCALHOST = "152.96.214.132"
PORT = 9991

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock,coordinate_list)
    newthread.start()
