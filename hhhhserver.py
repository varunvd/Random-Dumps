import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 9009
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
v = conn.recv(1024)
v = str(v)

lista  = { 'a' : 'hope' , 'b' : 'it', 'c' : 'works'  }
lista.__delitem__(v)
json_file = json.dumps(lista)
conn.send(json_file)
conn.close()

