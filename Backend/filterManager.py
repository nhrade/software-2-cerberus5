#!/usr/bin/env python3
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os, scapyUtilities, filterInterception, atexit, queue


saveIPTables = "iptables-save > savedIPTables.txt"
interceptorIPTables = "iptables -R OUTPUT 1 -j NFQUEUE"
restoreIPTables = "iptables-restore < savedIPTables.txt"
backupRestore = "iptables-restore < backupIPTables.txt"
maxLength = 100
interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
savedQueue = []#queue.Queue(maxLength)

def toggleInterception(intercept):
	global interceptor, savedQueue
	
	if intercept and not interceptor.isAlive() and scapyUtilities.snifferIsAlive():
		if savedQueue:#.empty():
			savedQueue.clear()#queue.clear()
			#savedQueue = None
		interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
		os.system(saveIPTables)
		os.system(interceptorIPTables)
		interceptor.start()
		
	else:
		os.system(restoreIPTables)
		savedQueue = interceptor.intercepted_packets()
		print("saving intercepted")
		print(len(savedQueue))
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
	interceptor.forward(file_, packet)

	
def forwardPacketList(num=1,newQueue=[]):
	global savedQueue
	file_ = "livePacket.pcap"
	open(file_, 'w').close()
	print(len(savedQueue))
	print("size of saved")
	if newQueue:
		print("recieved queue")
		savedQueue = newQueue
	interceptor.forward_packet(file_,num,savedQueue)
	
def dropPacket(num=1):
	interceptor.dropPacket(num,savedQueue)

def getInternalQueue():
	intercepted = interceptor.intercepted_packets()
	if savedQueue:
		intercepted = savedQueue
	print(len(intercepted))
	print(len(savedQueue))
	for elem in intercepted:
		print(elem)

atexit.register(toggleInterception, False)
