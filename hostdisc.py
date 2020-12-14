import socket

for i in range(1,20):
       print("Starting...\n")
       i = str(i)
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
          s.settimeout(3)
          s.connect(("192.168.1.%s" %i , 21))
          print("Connecting to %s" %i)
          s.settimeout(None)
          resp = s.recv(4096)
          print(resp)
       except:
           print("connection error \n")
