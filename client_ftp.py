import socket
import sys
HOST = "3.82.215.99"  # The server's hostname or IP address
PORT = 9999  # The port used by the server
PATH="file.bin"
s = socket.socket()
s.connect((HOST,PORT))
f = open(PATH,'wb') #open in binary    
while(True): 
    print(">>Reading Data from server")
    l = sc.recv(1024)
    while (l):
        f.write(l)
        l = sc.recv(1024)
    f.close()
    sc.close()
    print(">>File saved")
s.close()