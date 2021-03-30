# SENDER.PY
# LAURIE DELINOIS, MARCUS WONG
# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time

#s = socket(AF_INET,SOCK_DGRAM)
#sys.stdin.readline()
host =sys.argv[1]
#port = 9999
port = int(sys.argv[2])

s = socket(AF_INET,SOCK_DGRAM)
buf =1024
addr = (host,port)
#inFile = sys.argv[1]


#f=open("a.txt","rb")
#f = open("a.txt", "rb")

#data = f.read(buf).encode()
data = sys.stdin.read(buf).encode()
start_time = time.time()
total_kb = 0
timeSec = 0

while (data):
  #for line in sys.stdin:  
    sys.stdin.read(buf)
    if(s.sendto(data,addr)):
      #for line in sys.stdin: 
        print("sending ...")
        data = sys.stdin.read(buf).encode()
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_kb = total_kb + 1
        
      #for line in sys.stdin:
        #data = f.read(buf)
      
s.close()
print("File received, exiting.")

#rate = (total_kb / 125) / timeSec
#rate = float("%0.3f" % (rate))
elapsed_time = float("%0.3f" % (elapsed_time))
bytes = total_kb * 1000
print("Sent " + str(bytes) + " bytes in " + str(elapsed_time) + " seconds: " + str(total_kb) + " kB/s")
