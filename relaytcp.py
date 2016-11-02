#!/usr/bin/python3
# iMatic 8 Relay TCP interface

import time
import os
import sys
import socket

def networkrelay(relay, state):
    if relay in ("ALL","All","all",):
        if state in ("ON","On","on"):
            msg = (b'\xFD\x02\x20\xF8\x88\x5D')
        elif state in ("OFF","Off","off"):
            msg = (b'\xFD\x02\x20\xF8\x80\x5D')        
    elif relay in ("1","2","3","4","5","6","7","8"):
        if state in ("ON","On","on"):
            if relay == "1":
                msg = (b'\xFD\x02\x20\x01\x01\x5D')
            if relay == "2":
                msg = (b'\xFD\x02\x20\x02\x01\x5D')
            if relay == "3":
                msg = (b'\xFD\x02\x20\x03\x01\x5D')
            if relay == "4":
                msg = (b'\xFD\x02\x20\x04\x01\x5D')
            if relay == "5":
                msg = (b'\xFD\x02\x20\x05\x01\x5D')
            if relay == "6":
                msg = (b'\xFD\x02\x20\x06\x01\x5D')
            if relay == "7":
                msg = (b'\xFD\x02\x20\x07\x01\x5D')
            if relay == "8":
                msg = (b'\xFD\x02\x20\x08\x01\x5D')
        elif state in ("OFF","Off","off"):
            if relay == "1":
                msg = (b'\xFD\x02\x20\x01\x00\x5D')
            if relay == "2":
                msg = (b'\xFD\x02\x20\x02\x00\x5D')
            if relay == "3":
                msg = (b'\xFD\x02\x20\x03\x00\x5D')
            if relay == "4":
                msg = (b'\xFD\x02\x20\x04\x00\x5D')
            if relay == "5":
                msg = (b'\xFD\x02\x20\x05\x00\x5D')
            if relay == "6":
                msg = (b'\xFD\x02\x20\x06\x00\x5D')
            if relay == "7":
                msg = (b'\xFD\x02\x20\x07\x00\x5D')
            if relay == "8":
                msg = (b'\xFD\x02\x20\x08\x00\x5D')
    else:
       print ("relaytcp.py invalid value !"), sys.exit(0);
    ######################################################
    host = '192.168.1.4'
    port = 30000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.sendall(msg)
    ret = s.recv(1024)
    s.close()
##########################################################
if __name__ == "__main__":
    input1 = input("Wich Relay? (1 -8 or All): ")
    input2 = input("On or Off?: ")
    networkrelay(input1, input2)
