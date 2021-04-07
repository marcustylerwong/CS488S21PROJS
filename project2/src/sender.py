# SENDER.PY
# LAURIE DELINOIS, MARCUS WONG
# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time
import json
import base64



<<<<<<< HEAD
=======
  
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
host =sys.argv[1]
port = int(sys.argv[2])

s = socket(AF_INET,SOCK_DGRAM)
#s.setblocking(0)
buf =1024
addr = (host,port)
<<<<<<< HEAD
#counter = 0
=======
counter = 0
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69

#f=open("a.txt","rb")
#f = open("a.txt", "rb")


#possibly needs to take this in as a string for packet and not be encoded already?
#no, simply send buffer size to packet instead of having it read in directly

#data = sys.stdin.read(buf).encode()

#write data in from command line
<<<<<<< HEAD

data = sys.stdin.read().encode()

"""
start_time = time.time()
total_kb = 0
"""
#-----------------------------make packets-----------------------------------
def create_packet(data):


  #array = bytearray(data.encode()) #bug here with setting up packet split
  #packet = [array[i:i + 1024] for i in range(0, len(array), 1024)]
 # header = datagram(data)

  #make the data into a list of bytes to iterate through
  seqnum = 0

  new_seqnum = str(seqnum)

  b_arr = bytearray(data)
  b_arr.append(seqnum)


  #array = bytearray(data)
  #pass data into packet object
  packet = [b_arr[i:i + buf] for i in range(0, len(b_arr), buf)]
  #https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks/312464#312464
  #packets = packet + header

  return packet

#packets = create_packet(data)
#arr_index = 0

"""
#--------------------------------make header-------------------------

def datagram(packets):

  seqnum = 0
  #header = {'seqnum' : seqnum}
  pack = {'packets': packets, 'seqnum': seqnum}

  rudp = header.get('seqnum')
  return pack

#-------------------------------header done------------------------------
"""

#data = sys.stdin.read(buf).encode()
=======
data = sys.stdin.read().encode()

>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69

start_time = time.time()
total_kb = 0
seqnum = 0
packets = create_packet(data)

<<<<<<< HEAD
arr_index = 0
#seqnum = 0
ACK = " "
s.settimeout(0.5)
#header = datagram(data)
#pack = {'packets' : packets[arr_index], 'seqnum' : seqnum}
#while(data):

while (arr_index < len(packets)):
    """ idea: have packets and sequence numbers in the same dictionary """



    #packets are written into dictionary with sequence number attached to array index
    #pack = {"packets" : packets[arr_index], "seqnum" : seqnum}
   # pack = {str(seqnum) : packets}
    #datagram = {'seqnum' : seqnum}
    #encoded_dict = json.dumps(pack).encode('utf-8')
    #encoded_dict = str(pack.get('packets')).encode('utf-8')

    #message = str(pack)
    #encoded_dict = str(pack).encode('ascii')
    #encoded_dict = message.encode('ascii')
    #pack_encoded_byte = base64.b64encode(encoded_dict)

    #if(s.sendto(packets[arr_index],addr)):

    if(s.sendto(packets[arr_index], addr)):
    #if(s.sendto(encoded_dict, addr)):
    #if(s.sendto(pack_encoded_byte, addr)):
    #if(s.sendto(pack.get('packets'), addr)):
    #if(s.sendto(pack_encoded_byte, addr)):





        #print("sending ...")
        arr_index = arr_index + 1
        #seqnum = arr_index
        seqnum += 1
        #keep track of time and total kb
=======
#-----------------------------make packets-----------------------------------
def create_packet(data, buf):
  
  
  #array = bytearray(data.encode()) #bug here with setting up packet split
  #packet = [array[i:i + 1024] for i in range(0, len(array), 1024)]
 # header = datagram(data)
  
  #make the data into a list of bytes to iterate through
  b_arr = bytearray(data)
  #array = bytearray(data)
  #pass data into packet object
  packet = [b_arr[i:i + buf] for i in range(0, len(b_arr), buf)] 
  #https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks/312464#312464
  #packets = packet + header
  
  return packet

#packets = create_packet(data)
#arr_index = 0

#--------------------------------make header-------------------------
def datagram(packets):
  
  seqnum = 0
  #header = {'seqnum' : seqnum}
  pack = {'packets': packets, 'seqnum': seqnum}
  
  rudp = header.get('seqnum')
  return pack

#-------------------------------header done------------------------------
#data = sys.stdin.read(buf).encode()
packets = create_packet(data, buf)

arr_index = 0
seqnum = 0
#header = datagram(data)
#pack = {'packets' : packets[arr_index], 'seqnum' : seqnum}
#while(data):
while (arr_index < len(packets)):  
    """ idea: have packets and sequence numbers in the same dictionary """
    
    #acknowledged = False
    
    #packets are written into dictionary with sequence number attached to array index
    pack = {'packets' : packets[arr_index], 'seqnum' : seqnum}
    #pack = str(pack)
    #if(s.sendto(packets[arr_index],addr)):
    
    if(s.sendto(pack.get('packets'), addr)):
    
    
    #if(s.sendto(data,addr)):
      #s.sendto(bytearray(buf),addr)
        
        print("sending ...")
        arr_index = arr_index + 1
        seqnum = arr_index
        
        
        print("Sequence Number: " + str(pack.get('seqnum')))
        
        
        
        acknowledged = False
        #must use recvfrom here to check that acknowledgements are received
        #waiting to receive ack from receiver
        #while not acknowledged: #while acknowledged is true
        while acknowledged:
          try:
            data, addr = s.recvfrom(1024)
           
            acknowledged = True
            print("Ack")
          except timeout:
            s.settimeout(2)
        #print (ACK)
            #print("Ack")
       
        #recognize ack from receiver
        
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_kb = total_kb + 1

        #print("Sequence Number: " + str(pack.get('seqnum')))
        print("Sequence Number: " + str(seqnum))

       #--------------------------------------------------------------don't touch for now-----------------------------------------------------------

        acknowledged = False
        #must use recvfrom here to check that acknowledgements are received
        #waiting to receive ack from receiver
        #while not acknowledged: #while acknowledged is true
        while not acknowledged:
          try:
            ACK, addr = s.recvfrom(1024)

            acknowledged = True

            #print("Ack Received")
          except timeout:
            s.sendto(packets[arr_index], addr)
            #s.sendto(pack.get('packets'), addr)
            #s.settimeout(2)
        print (ACK)

        #----------------------------------------------------------don't touch for now------------------------------------------------------------------

            #print("Ack")

        #recognize ack from receiver
        """
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_kb = total_kb + 1
      """
s.close()

sys.stderr.write("All acks received.\n")

elapsed_time = float("%0.3f" % (elapsed_time))
bytes = total_kb * 1024
kb_sec = total_kb/elapsed_time
kb_sec = float("%0.3f" % (kb_sec))
print("Sent " + str(bytes) + " bytes in " + str(elapsed_time) + " seconds: " + str(kb_sec) + " kB/s")
<<<<<<< HEAD
print("Packets sent: " + str(arr_index))
=======
print("Packets sent: " + str(arr_index))
>>>>>>> 2eb904767bf67acdcc95f6faecdf729c6a7b8f69
