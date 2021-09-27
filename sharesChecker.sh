#!/bin/bash

while read -r line; do
	smbmap -H $line

done < $1
