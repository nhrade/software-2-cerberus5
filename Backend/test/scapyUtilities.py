#!/usr/bin/env python3
from scapySniffer import *

#unpacks a PCAP file into a list of lists of layers (packets)
def unpackPCAP(file_):
	packets = rdpcap(file_)

	pkts = list()
	for packet in packets.res:
		l=list(dissectLayers(packet))
		":".join(str(l))
		c=str(packet.show)

		layers = dict()
		for layer in l:
			fieldsAndValues = dict()
			try:
				for field in packet[layer].fields_desc:
					#print(field.name)
					if field.name== 'qd':
					#		print(str(packet['DNS'].qd.qname))
							val = str(packet['DNS'].qd.qname)
					else:
					#		print(getattr(packet[layer], field.name)) 
						val = getattr(packet[layer], field.name)
					fieldsAndValues[field.name] = val
			except:
				continue
				
			layers[layer] = fieldsAndValues

		print(packet.show())
		pkts.append(layers)

	return packets.res, pkts

#extracts the different layers within a packet by traversing each packet's contents
def dissectLayers(packet):
	yield packet.name
	while packet.payload:
		packet = packet.payload
		yield packet.name

#produces packet in hexidecimal format
def hexDump(packet):
	return hexdump(packet)

#produces packet in "binary" format
def binaryDump(packet):
    return raw(packet)

#edits the field of a packet layer
def editFields(packet,layer,field, value):
	setattr(packet[layer], field, value)
    
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

