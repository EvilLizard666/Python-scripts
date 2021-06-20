#!/usr/bin/python3 

from ftplib import FTP
import sys

hosts = open(sys.argv[1], 'r')
r = hosts.readlines()
for item in r:
    print("[+] Connecting to: %s" %item)
    try:
        
        ftp = FTP(item, timeout=3)   
        ftp.login()
        if ftp.retrlines('LIST') != 0:
            print("[+] Anonymous login enabled in Host:%s " %item)
            ftp.quit()            
        else:
            print("[+] Anonymous is not enabled\nHost: %s" %item)
    except:
        print("Unable to connect to: %s" %item)
        
