#!/usr/bin/env python3
from netfilterqueue import NetfilterQueue
from scapy.all import *
from scapyUtilities import getFilter
import os

saveIPTables = "iptables-save > savedIPTables.txt"
interceptorIPTables = "iptables -A FORWARD -j NFQUEUE"
restoreIPTables = "iptables-restore < savedIPTables.txt"

def toggleInterception(intercept):
	if intercept:
		os.system(saveIPTables)
		os.system(interceptorIPTables)
	else:
		os.system(restoreIPTables)

#def intercepting()
