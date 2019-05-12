#!/usr/bin/env python3
from scapySniffer import *

def unpackPCAP(file_):
	packets = rdpcap(file_)
	layerList=list()
	layerContentList=list()
	for packet in packets.res:
		r=list(dissectLayers(packet))
		":".join(str(r))
		c=str(packet.summary())

		layerList.append(r)
		layerContentList.append(c)
	"""test code for verification of list of lists of layers in packets
	for pack in layerList:
		print(pack)
	for data in layerContentList:
		print(data)
	"""
	return layerList, layerContentList

def dissectLayers(packet):
	yield packet.name
	while packet.payload:
		packet = packet.payload
		yield packet.name

def dissectData(packet):
    yield packet
    while packet.payload:
        packet = packet.payload
        yield packet
    
#unpackPCAP('2019-05-09_17.31.pcap')

filter__ = ""
sniffer = Sniffer(filter__)

def addFilter(filter_):
	print("At Filter")
	global sniffer, filter__
	if sniffer.isAlive():
		return
	filter__ = filter_
	sniffer = Sniffer(filter__)
	print("modified filter")

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
		
def getFilter()
	return filter__

