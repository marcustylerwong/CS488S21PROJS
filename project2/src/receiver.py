# Marcus Wong, Laurie Delinois
# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import time
<<<<<<< HEAD
import json
import base64
import struct





#------------------------------------running main program------------------------------
#sys.argv for testing
host = sys.argv[1]
#host = "127.0.0.1"
port = int(sys.argv[2])
#port = int(sys.argv[1])
=======


  
  
  

#------------------------------------running main program------------------------------
#sys.argv for testing
#host = sys.argv[1]
host = "127.0.0.1"
#port = int(sys.argv[1])
port = int(sys.argv[1])
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69

#start socket and bind to sender
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024
counter = 0
<<<<<<< HEAD
seqnum = 0
=======
seqnum = counter
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
ack = "Acknowledgement"

#f = open("received.txt",'wb')

data,addr = s.recvfrom(buf)
#here, we need to set data equal to just the packet end of the dictionary, which requires decoding the packet to reprint it here
#data = data.decode()
#packet = data.decode().get('packets')
#decoded_dict = str(data).decode('utf-8')

#decoded = base64.b64decode(data)

#decoded_ascii = decoded.decode('ascii')

#decoded_ascii = decoded_ascii.replace("'", "\"")

#decoded_dict = json.loads(decoded_ascii) #this converts the input data from dict to encoded bytes to dict
"""
ip_header = data.decode()[0:20]
udp_header = data.decode()[20:28]
packet = data.decode()[30:]
#header = struct.unpack('!BBHHHBBH4s4s', udp_header)
"""


try:
    while(data):
<<<<<<< HEAD
       #so this end is receiving the packet as a dictionary, but is writing the dictionary itself to the file rather than the packets, which is incorrect
       #decoded = base64.b64decode(data)
       #sys.stdout.write(data.decode())
       sys.stdout.write(data.decode())

       #decoded_dict = (data.decode())
       #decoded_dict = data.decode('seqnum')
       #sys.stderr.write(decoded_dict + " \n")
       #data,addr = s.recvfrom(buf)
       #counter = counter + 1
       seqnum = seqnum + 1

       s.settimeout(3)

=======
       
       sys.stdout.write(data.decode())
       #data,addr = s.recvfrom(buf)
       counter = counter + 1
       seqnum = counter
    
       s.settimeout(3)
    
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
       data,addr = s.recvfrom(buf)
       #sys.stderr.write(str(data))
       #if(s.recvfrom()):
       #sys.stderr.write(str(seqnum) + " ")
       #if(s.recvfrom(buf)):
<<<<<<< HEAD

       if(s.sendto(bytes(ack, 'utf-8'), addr)):
         sys.stderr.write( ack  + "  " + str(seqnum) + " \n ")
         #sys.stderr.write("ack is working \n")
           #sys.stderr.write("Packet received.\n")
    #s.close



       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
    #print("Server Ack: " + ack)


       #send ack to sender
       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
        # print("Server Ack: " + ack)


=======
      
       if(s.sendto(bytes(ack, 'utf-8'), addr)):
         sys.stderr.write( ack  + "  " + str(seqnum) + " \n ")
           #sys.stderr.write("Packet received.\n")
    #s.close
      
       
       
       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
    #print("Server Ack: " + ack)
       
       
       #send ack to sender
       #if(s.sendto(bytes(ack, 'utf-8'), addr)): # this sends the acknowledgement
        # print("Server Ack: " + ack)
      
         
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
       #sys.stderr.write("Data: " + str(data.decode()) + "Sequence Number: " + str(seqnum))
        #f.write(data)
        #s.sendto(data,addr)

except timeout:
    s.close()
    sys.stderr.write("File Received, exiting.\n")
<<<<<<< HEAD
    #sys.stderr.write(decoded_dict)



#------------------------------main program end----------------------------------------
=======
    
  
  
#------------------------------main program end----------------------------------------
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
