#!/usr/bin/env python3
from scapySniffer import *
from scapy.all import *
import os, atexit, filterManager

saveIPTables_ = "iptables-save > savedIPTables2.txt"
snifferIPTables = "iptables -A OUTPUT -j NFQUEUE --queue-num 1"
restoreIPTables_ = "iptables-restore < savedIPTables2.txt"
backupRestore_ = "iptables-restore < backupIPTables.txt"
#unpacks a PCAP file into a list of lists of layers (packets). Returns list of Scapy packets and list of packet data for easy printing
def unpackPCAP(file_):
	packets = rdpcap(file_)
	pkts = list()
	
	for packet in packets.res:
		pkts.append(dissectPacket(packet))

	return packets.res, pkts

#extracts the different layers within a packet by traversing each packet's contents
def dissectLayers(packet):
	yield packet.name
	while packet.payload:
		packet = packet.payload
		yield packet.name

#produces packet in hexidecimal format
def hexDump(packet):
	s = str(packet)
	":".join("{:02x}".format(ord(c)) for c in s)
	return s
    #return str(binaryPacket)#hexPkt = hexdump(packet)

#produces packet in "binary" format
def binaryDump(packet):
    binaryPacket = raw(packet)
    return str(binaryPacket)

#edits the field of a packet layer
def editFields(packet,layer,field, value):
	setattr(packet[layer], field, value)
# dissects Packets and returns a list of the layer dictionaries that contain fields and field values.	
def dissectPacket(packet):
	packetData = list()
	l=list(dissectLayers(packet))
	":".join(str(l))

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

	#print(packet.show())
	packetData.append(layers)
	return packetData

    
#packets, pktsData = unpackPCAP('2019-05-09_17.31.pcap')
#s= hexDump(packets[1])
#print(s)

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
		try:
			os.system(saveIPTables_)
			os.system(snifferIPTables)
			sniffer.start()
		except:
			os.system(restoreIPTables_)
	else:
		print("[*] Stop sniffing")
		filterManager.toggleInterception(False)
		os.system(restoreIPTables_)
		if sniffer.isAlive():
			sniffer.join(2.0)
#		""""if sniffer.isAlive():
#			sniffer.socket.close()""""
		sniffer = Sniffer(filter__)
		
def getFilter():
	return filter__
	
def snifferIsAlive():
	return sniffer.isAlive()
	
atexit.register(toggleTheSniffer, False)

