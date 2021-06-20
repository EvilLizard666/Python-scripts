import socket

print("[+] Starting...\n")
for i in range(0,254):
       
       i = str(i)
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
          s.settimeout(3)
          s.connect(("192.168.1.%s" %i , 22))
          print("Connected to 192.168.1.%s " %i)
          s.settimeout(None)
          resp = s.recv(4096)
          print(resp)
       except:
           print("Host:192.168.1.%s\nPort=22 Closed!\n" %i) 
