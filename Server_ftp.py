import socket
import sys
s = socket.socket()
s.bind(("",9999))
s.listen(1) # Acepta hasta 10 conexiones entrantes.
PATH="files.bin"

while True:
    print(">>Opening file again")
    f = open(PATH,'rb') #open in binary
    l = f.read(1024)
    sc, address = s.accept()
    print (address)
    print(">>Sending data")
    while(l):
        sc.send(l)
        l=f.read(1024)
    f.close()
    sc.close()
    print(">>Data sent")
s.close()