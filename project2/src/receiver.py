# Marcus Wong, Laurie Delinois 
# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select

#host = sys.argv[1]
host = "127.0.0.1"
port = int(sys.argv[1])

#start socket and bind to sender
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024


#f = open("received.txt",'wb')

data,addr = s.recvfrom(buf)


try:
    while(data):
       sys.stdout.write(data.decode())
       #f.write(data)
       s.settimeout(2)
       data,addr = s.recvfrom(buf)
        #f.write(data)
        #s.sendto(data,addr)
    
except timeout:
    s.close()
    sys.stderr.write("File Received, exiting.\n")
