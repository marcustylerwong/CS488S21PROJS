# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select

#host="0.0.0.0"
#host =sys.argv[1]
host = sys.argv[1]
port = int(sys.argv[2])
#port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
#addr = (port)
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
    #print("File Received, exiting.")
