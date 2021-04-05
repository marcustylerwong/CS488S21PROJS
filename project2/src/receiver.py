# Marcus Wong, Laurie Delinois 
# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import time


  
  
  

#------------------------------------running main program------------------------------
#sys.argv for testing
#host = sys.argv[1]
host = "127.0.0.1"
#port = int(sys.argv[1])
port = int(sys.argv[1])

#start socket and bind to sender
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024
counter = 0
seqnum = counter
ack = "Acknowledgement"

#f = open("received.txt",'wb')

data,addr = s.recvfrom(buf)


try:
    while(data):
       
       sys.stdout.write(data.decode())
       #data,addr = s.recvfrom(buf)
       counter = counter + 1
       seqnum = counter
    
       s.settimeout(3)
    
       data,addr = s.recvfrom(buf)
       #sys.stderr.write(str(data))
       #if(s.recvfrom()):
       #sys.stderr.write(str(seqnum) + " ")
       #if(s.recvfrom(buf)):
      
       if(s.sendto(bytes(ack, 'utf-8'), addr)):
         sys.stderr.write( ack  + "  " + str(seqnum) + " \n ")
           #sys.stderr.write("Packet received.\n")
    #s.close
      
       
       
       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
    #print("Server Ack: " + ack)
       
       
       #send ack to sender
       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
        # print("Server Ack: " + ack)
      
         
       #sys.stderr.write("Data: " + str(data.decode()) + "Sequence Number: " + str(seqnum))
        #f.write(data)
        #s.sendto(data,addr)
    
except timeout:
    s.close()
    sys.stderr.write("File Received, exiting.\n")
    
  
  
#------------------------------main program end----------------------------------------