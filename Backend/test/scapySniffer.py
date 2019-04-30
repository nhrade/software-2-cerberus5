#!/usr/bin/env python3
#https://github.com/secdev/scapy/issues/989 guedou and HenninhCash
from scapy.all import*
import select
import datetime
import time, threading

# s = conf.L2listen()
#capture = False
now = datetime.datetime.now()
captureFilter = ""
capture = threading.Event()
#file_ = ""

def proxyOn(capture):
	print("At ProxyOn")
	if capture:
		file_ = str(now.strftime("%Y-%m-%d_%H.%M"))+'.pcap'
		f = open(file_, 'w').close
		captureLiveTraffic(capture, file_)
		return
	else:
		return
def captureLiveTraffic(capture, file_):
	print("Capturing Packet" + file_  +'\n')
	print(capture)
	

	if capture:
		#packets = 
		sniff(filter = captureFilter,prn = recieveFileName(file_))#, stop_filter=lambda p: capture.is_set())
	#packets = None
	return

def recieveFileName(file_ : str):
	print(file_ + 'file recieved\n')
	def appendToPcap(capturedPacket):
		print('Writing To PCAP' + file_)
		capturedPacket.show()
		wrpcap(file_, capturedPacket, append = True)
	return appendToPcap
	




#t = threading.Thread(target=captureLiveTraffic, args=(capture,))
#t.start()

#time.sleep(3)
#print("Shutdown")
#capture.set()

#while True:
#	t.join(2)
#	if t.is_alive():
#		print("Still Running")
#	else:
#		break
#print("shutdown")
