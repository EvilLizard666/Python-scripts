#!/bin/bash

echo -e "\e[92m                   _____
     __ _____     /     \     
/ \ |  |__   |   /       \    
| | |  |  / /   /  _____  \  
| |_|  | / /_  /  /     \  \ 
(___|__|/____|/__/       \__\ RD "

read -p  "[+] Target ip = " ip              #Input target ip
read -p  "[+] File path to save nmap scan = " nmap
read -p  "[+] File to save nikto scan = " nikto




xterm -hold -e nmap -sC -sV $ip -o $nmap | xterm -hold -e nikto -h $ip | xterm -hold -e dirb http://$ip/
