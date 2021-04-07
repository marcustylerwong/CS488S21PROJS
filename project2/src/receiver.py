# Marcus Wong, Laurie Delinois 
# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import time
import json
import base64
import struct

  
  
  

#------------------------------------running main program------------------------------
#sys.argv for testing
host = sys.argv[1]
#host = "127.0.0.1"
port = int(sys.argv[2])
#port = int(sys.argv[1])

#start socket and bind to sender
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024
seqnum = 0
ack = "Acknowledgement"



data,addr = s.recvfrom(buf)

#here, we need to separate the data brought in to two separate objects for data and seqnum
#then compare seqnum of received data to counter within receiver



try:
    while(data):
       #write decoded data to file
     
       sys.stdout.write(data.decode())
       
       #increment counter
       seqnum = seqnum + 1
    
       s.settimeout(3)
    
       #receive data from sender and send acknowledgement
       data,addr = s.recvfrom(buf)
       
       if(s.sendto(bytes(ack, 'utf-8'), addr)):
         sys.stderr.write( ack  + "  " + str(seqnum) + " \n ")
         
         sys.stderr.write("Packet received.\n")
    
    
except timeout:
    s.close()
    sys.stderr.write("File Received, exiting.\n")
    #sys.stderr.write(decoded_dict)
    
  
  
#------------------------------main program end----------------------------------------