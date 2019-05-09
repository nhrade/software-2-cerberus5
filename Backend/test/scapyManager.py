#!/usr/bin/env python3
from scapySniffer import proxyOn
from scapy.all import *

capture = False
unpackPCAP()
while True:
	inp = input("input if capture \n")
	print(inp)
	if inp == "yes":
		capture = True
	else:
		capture = False
	print(capture)
	proxyOn(capture)



def unpackPCAP(file_):
    packets = rdpcap(file_)
    print(type(packets))

def retrievePacket():
