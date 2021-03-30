# SENDER.PY
# LAURIE DELINOIS, MARCUS WONG
# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import time


host =sys.argv[1]

port = int(sys.argv[2])

s = socket(AF_INET,SOCK_DGRAM)
buf =1024
addr = (host,port)

#f=open("a.txt","rb")
#f = open("a.txt", "rb")


data = sys.stdin.read(buf).encode()
start_time = time.time()
total_kb = 0
timeSec = 0

while (data):  
    sys.stdin.read(buf)
    if(s.sendto(data,addr)):
      #for line in sys.stdin: 
        print("sending ...")
        data = sys.stdin.read(buf).encode()
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_kb = total_kb + 1
      
s.close()

elapsed_time = float("%0.3f" % (elapsed_time))
bytes = total_kb * 1024
kb_sec = total_kb/60
kb_sec = float("%0.3f" % (kb_sec))
print("Sent " + str(bytes) + " bytes in " + str(elapsed_time) + " seconds: " + str(kb_sec) + " kB/s")
