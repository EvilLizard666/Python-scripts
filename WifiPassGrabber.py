import re
import subprocess
import os
import sys

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
if len(profile_names) != 0:
    for name in profile_names:
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name , "key=clear"], capture_output = True).stdout.decode()
        reGex_output = (re.findall("Key Content            :(.*)\r", profile_info))
        ssid = (re.findall("SSID name              :(.*)\r", profile_info))
        final = ssid + reGex_output
        print(final)

         
        

            

