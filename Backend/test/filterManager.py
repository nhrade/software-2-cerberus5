#!/usr/bin/env python3
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os, scapyUtilities, filterInterception
import interceptionQueue

saveIPTables = "iptables-save > savedIPTables.txt"
interceptorIPTables = "iptables -A OUTPUT -j NFQUEUE"
restoreIPTables = "iptables-restore < savedIPTables.txt"
maxLength = 100
interceptor = filterInterception.Interceptor(scapyUtilities.getFilter(), maxLength)
interceptedQueue = interceptionQueue.Intercepted()

def toggleInterception(intercept):
	if intercept:
		os.system(saveIPTables)
		os.system(interceptorIPTables)
		interceptor.start()
		
	else:
		os.system(restoreIPTables)
		interceptor.join(2.0)

def setQueueLength(size):
	global maxLength, interceptor
	maxLength = size
	interceptor = filterInterception.Interceptor(scapyUtlities.getFilter(), maxLength)
