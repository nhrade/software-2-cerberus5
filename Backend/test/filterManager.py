#!/usr/bin/env python3
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os, scapyUtilities, filterInterception, atexit


saveIPTables = "iptables-save > savedIPTables.txt"
interceptorIPTables = "iptables -A OUTPUT -j NFQUEUE"
restoreIPTables = "iptables-restore < savedIPTables.txt"
backupRestore = "iptables-restore < backupIPTables.txt"
maxLength = 100
interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
savedQueue = None

def toggleInterception(intercept):
	global interceptor, savedQueue
	
	if intercept and not interceptor.isAlive():
		if not savedQueue.empty():
			savedQueue.queue.clear()
			savedQueue = None
		interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
		os.system(saveIPTables)
		os.system(interceptorIPTables)
		interceptor.start()
		
	else:
		os.system(restoreIPTables)
		savedQueue = interceptor.intercepted_packets()
		if interceptor.isAlive():
			interceptor.join(1.0)
		#if interceptor.isAlive():
		#	os.system(backupRestore)
		#	interceptor.socket.close()
		#if not interceptor.isAlive():
		print("resetting interceptor")
		interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
		

def setQueueLength(size):
	global maxLength, interceptor
	maxLength = size
	interceptor = filterInterception.Interceptor(scapyUtlities.getFilter(), maxLength)

def forwardPacket(packet):
	file_ = "livePCAP.pcap"
	open(file_, 'w').close()
	interceptor.forward_packet(file_, packet)

	
def forwardPacketList(num=1):
	file_ = "livePacket.pcap"
	open(file_, 'w').close()
	interceptor.forward(file_,num,savedQueue)
	
def dropPacket(num=1):
	interceptor.dropPacket(num,savedQueue)

def getInternalQueue():
	intercepted = interceptor.intercepted_packets()
	if savedQueue is not None:
		intercepted = savedQueue
	print(intercepted)
	print(savedQueue)
	for elem in list(intercepted.queue):
		print(elem)

atexit.register(toggleInterception, False)
