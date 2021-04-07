# SENDER.PY
# LAURIE DELINOIS, MARCUS WONG
# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time
import json
import base64


  
host =sys.argv[1]
port = int(sys.argv[2])

s = socket(AF_INET,SOCK_DGRAM)
#s.setblocking(0)
buf =1024
addr = (host,port)



#possibly needs to take this in as a string for packet and not be encoded already?
#no, simply send buffer size to packet instead of having it read in directly


#write data in from command line
data = sys.stdin.read().encode()

"""
start_time = time.time()
total_kb = 0
"""
#-----------------------------make packets-----------------------------------
def create_packet(data, buf):
  
  #make the data into a list of bytes to iterate through
  seqnum = 0
 
  new_seqnum = str(seqnum)

  b_arr = bytearray(data)
  s_arr = bytearray(seqnum)
  
  #send bytearray with sequence number
  #b_arr.append(seqnum)
  
  #add seqnum array and data bytearray
  b_arr += s_arr
  
  
  
  #pass data into packet object
  packet = [b_arr[i:i + buf] for i in range(0, len(b_arr), buf)]
  #https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks/312464#312464
  #packets = packet + header
  
  return packet


start_time = time.time()
total_kb = 0
seqnum = 0
packets = create_packet(data, buf)

arr_index = 0
ack = " "
s.settimeout(0.5)

while (arr_index < len(packets)):  
    """ idea: have packets and sequence numbers in the same dictionary """
    
    
    #packets are written into dictionary with sequence number attached to array index
    #pack = {"packets" : packets[arr_index], "seqnum" : seqnum}
    
    if(s.sendto(packets[arr_index], addr)):
        arr_index = arr_index + 1
        seqnum = arr_index
       
        
        
        #keep track of time and total kb
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_kb = total_kb + 1
        
        #print("Sequence Number: " + str(pack.get('seqnum')))
        print("Sequence Number: " + str(seqnum))
        
       #--------------------------------------------------------------for receiving acknowledgements----------------------------------------------------------- 
       
       #set false flag
        ack_flag = False
        
        #waiting to receive ack from receiver
        
        while not ack_flag:
          try:
            ack, addr = s.recvfrom(1024)
           
            ack_flag = True 
            
            #print("Ack Received")
          except timeout:
            s.sendto(packets[arr_index], addr)
            #s.sendto(pack.get('packets'), addr)
            s.settimeout(2)
        print (ack)
        
        #----------------------------------------------------------for receiving acks------------------------------------------------------------------
        
       
#close socket once all data sent and all acks received    
s.close()

sys.stderr.write("All acks received.\n")

elapsed_time = float("%0.3f" % (elapsed_time))
bytes = total_kb * 1024
kb_sec = total_kb/elapsed_time
kb_sec = float("%0.3f" % (kb_sec))
print("Sent " + str(bytes) + " bytes in " + str(elapsed_time) + " seconds: " + str(kb_sec) + " kB/s")
print("Packets sent: " + str(arr_index))