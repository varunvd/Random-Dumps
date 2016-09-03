import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 9009
s.connect((HOST, PORT))
key_value = raw_input("Enter the key value\n")
s.send(key_value)
data = s.recv(1024)
dat = json.loads(data)
print 'data from serve ' 
print dat
s.close()
