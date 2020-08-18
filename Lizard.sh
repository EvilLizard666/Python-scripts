#!/bin/bash

echo "                                                                                       HTBA                                                                                                     "      
echo "                                                                                      HTBHTB                                                    HTBHTBHTBHTBHTBA                                "
echo "HTBHTB                   HTBHTB  HTBHTBHTBHTBHTBHTBHTBHTBHTBAA                       HTBHTBAA                    HTBHTBHTBHTBHTBHTBAA           HTBHTBHTBHTBHTBHTB                              "
echo "HTBHTB                   HTBHTB  HTBHTBHTBHTBHTBHTBHTBHTBHTBA                       HTBHTBHTBA                   HTBHTBHTBHTBHTBHTBAA           HTBHTBHTBHTBHTBHTBA                             "
echo "HTBHTB                   HTBHTB  HTBHTBHTBHTBHTBHTBHTBHTBHTB                       HTBHTBHTBHTB                  HTBHTBHTBHTBHTBHTBAA           HTBHTBHTBHTBHTBHTBAA                            " 
echo "HTBHTB                   HTBHTB  HTBHTBHTBHTBHTBHTBHTBHTBAA                       HTBHTBHTBHTBAA                 HTBHTBA       HTBHTB           HTBHTBHTBHTBHTBHTBHTB                           "
echo "HTBHTB                   HTBHTB  HTBHTBHTBHTBHTBHTBHTBHTBA                       HTBHTBHTBHTBHTBA                HTBHTBA       HTBHTB           HTBHTBA      HTBHTBHTB                          "
echo "HTBHTB                   HTBHTB                HTBHTBHTBA                       HTBHTBAA  HTBHTBAA               HTBHTBA       HTBHTB           HTBHTBA      HTBHTBHTBA                         "
echo "HTBHTB                   HTBHTB               HTBHTBHTBA                       HTBHTBAA    HTBHTBAA              HTBHTBHTBHTBHTBHTBAA           HTBHTBA      HTBHTBHTBAA                        "
echo "HTBHTB                   HTBHTB              HTBHTBHTBA                       HTBHTBAA      HTBHTBAA             HTBHTBHTBHTBHTBHTBAA           HTBHTBA      HTBHTBHTBHTB                       " 
echo "HTBHTB                   HTBHTB             HTBHTBHTBA                       HTBHTBAA        HTBHTBAA            HTBHTB      HTBHTB             HTBHTBA      HTBHTBHTBHTBA                      " 
echo "HTBHTB                   HTBHTB            HTBHTBHTBA                       HTBHTBHTBHTBHTBHTBHTBHTBAA           HTBHTB       HTBHTB            HTBHTBA      HTBHTBHTBHTBAA                     "
echo "HTBHTB                   HTBHTB           HTBHTBHTBA                       HTBHTBHTBHTBHTBHTBHTBHTBHTBA          HTBHTB        HTBHTB           HTBHTBA      HTBHTBHTBHTBHTB                    "
echo "HTBHTB                   HTBHTB          HTBHTBHTBA                       HTBHTBAA              HTBHTBAA         HTBHTB         HTBHTB          HTBHTBHTBHTBHTBHTBHTBHTBHTB                     "
echo "HTBHTB                   HTBHTB         HTBHTBHTBA                       HTBHTBAA                HTBHTBAA        HTBHTB          HTBHTB         HTBHTBHTBHTBHTBHTBHTBHTBAA                      "
echo "HTBHTB                   HTBHTB        HTBHTBHTBA                       HTBHTBAA                  HTBHTBAA       HTBHTB           HTBHTB        HTBHTBHTBHTBHTBHTBHTBHTBA                       "
echo "HTBHTB                   HTBHTB       HTBHTBHTBA                       HTBHTBAA                    HTBHTBAA      HTBHTB            HTBHTB       HTBHTBHTBHTBHTBHTBHTBHTB                        "
echo "HTBHTBHTBHTBHTBHTBHTB    HTBHTB      HTBHTBHTBHTBHTBHTBHTBAA          HTBHTBAA                      HTBHTBAA     HTBHTB             HTBHTB      HTBHTBHTBHTBHTBHTBHTBAA                         "
echo "HTBHTBHTBHTBHTBHTBHTB    HTBHTB     HTBHTBHTBHTBHTBHTBHTBHTB         HTBHTBAA                        HTBHTBAA    HTBHTB              HTBHTB     HTBHTBHTBHTBHTBHTBHTBA                          "
echo "HTBHTBHTBHTBHTBHTBHTB    HTBHTB    HTBHTBHTBHTBHTBHTBHTBHTBA        HTBHTBAA                          HTBHTBAA   HTBHTB               HTBHTB    HTBHTBHTBHTBHTBHTBHTB                           "
echo "HTBHTBHTBHTBHTBHTBHTB    HTBHTB   HTBHTBHTBHTBHTBHTBHTBHTBAA       HTBHTBAA                            HTBHTBAA  HTBHTB                HTBHTB   HTBHTBHTBHTBHTBHTBAA                            "

read -p  "[+] Target ip = " ip              #Input target ip
read -p  "[+] File path to save nmap scan = " nmap
read -p  "[+] File to save nikto scan = " nikto




xterm -hold -e nmap -sC -sV $ip -o $nmap | xterm -hold -e nikto -h $ip | xterm -hold -e dirb http://$ip/
