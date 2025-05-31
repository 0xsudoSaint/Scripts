from os import system
import sys

def docurl(fptr):
    for i in fptr:
        system("curl -k --proxy http://localhost:8080 %s " % i)
fptr=open(sys.argv[1])
docurl(fptr)

