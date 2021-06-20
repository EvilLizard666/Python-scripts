import re
import subprocess
import sys


with open("part1.txt") as f1, open("part2.txt") as f2, open("part3.txt") as f3, open("part4.txt") as f4:
    if sys.argv[1] in f1.read():
        print("Part1: " + sys.argv[1])
        f1.close()
    elif sys.argv[1] in f2.read():
        print("part2: " + sys.argv[1])
        f2.close()
    elif sys.argv[1] in f3.read():
        print("part3: " + sys.argv[1])
        f3.close()
    elif sys.argv[1] in f4.read():
        print("part4: " + sys.argv[1])
        f4.close()
    else:
        print("Phone Number Not Found!")

