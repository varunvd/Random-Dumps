import socket
import json
import csv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 9009
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
v = conn.recv(1024)
v = str(v)
f = open(v,'r')
ff = csv.DictReader(f)
json_file = json.dumps( [ err for err in ff ] )
conn.send(json_file)
conn.close()
s.close()
