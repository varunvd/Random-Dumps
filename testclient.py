import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 9009
s.connect((HOST, PORT))
key_value = raw_input("Enter the csv file name\n")
s.send(key_value)
data = s.recv(1024)
print "The json format of the csv file received from the server"
dat = json.loads(data)
print dat
s.close()
