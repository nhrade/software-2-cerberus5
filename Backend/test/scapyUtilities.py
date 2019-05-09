#!/usr/bin/env python3
from scapySniffer import proxyOn
from scapy.all import *


def unpackPCAP(file_):
    packets = rdpcap(file_)
    print(type(packets))

capture = False
unpackPCAP('2019-05-08_22.40.pcap')

while True:
	inp = input("input if capture \n")
	print(inp)
	if inp == "yes":
		capture = True
	else:
		capture = False
	print(capture)
	proxyOn(capture)

