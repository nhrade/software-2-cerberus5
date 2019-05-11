#!/usr/bin/env python3
from skyplabs import *

def unpackPCAP(file_): 
	packets = rdpcap(file_)
	print(type(packets))

capture = False
#unpackPCAP('2019-05-08_22.40.pcap')
filter__ = ""
sniffer = Sniffer(filter__)

def addFilter(filter_):
	global sniffer, filter__
	filter__ = filter_
	sniffer = Sniffer(filter__)

def toggleTheSniffer(capture):
	print(capture)
	global sniffer
	if capture and not sniffer.isAlive():
		print("[*] Start sniffing...")
		sniffer.start()
	else:
		print("[*] Stop sniffing")
		if sniffer.isAlive():
			sniffer.join(2.0)
		if sniffer.isAlive():
			sniffer.socket.close()
		sniffer = Sniffer(filter__)


while True:
	inp = input("input if capture \n")
	print(inp)
	if inp == "yes":
		capture = True
	elif inp == "filter":
		filter_ = input("enter filter \n")
		addFilter(filter_)
	else:
		capture = False
	print(capture)
	#proxyOn(capture)
	toggleTheSniffer(capture)
