#!/usr/bin/env python3
from scapySniffer import proxyOn
from scapy.all import *


def unpackPCAP(file_):
	packets = rdpcap(file_)
	print(type(packets))
	
	for p in packets:
		print(p.summary())
#		getPacketLayers(p)
	#print(packets)

def getPacketLayers(packet):
	print(str(packet.getlayer()))
    



capture = False
unpackPCAP('2019-05-09_17.31.pcap')
sniffer = Sniffer()

def toggleTheSniffer(capture):
	print(capture)
	global sniffer
	if capture:
		print("[*] Start sniffing...")
		sniffer.start()
	else:
		print("[*] Stop sniffing")
		sniffer.join(2.0)

		if sniffer.isAlive():
			sniffer.socket.close()
		sniffer = Sniffer()


while True:
	inp = input("input if capture \n")
	print(inp)
	if inp == "yes":
		capture = True
	else:
		capture = False
	print(capture)
	#proxyOn(capture)
