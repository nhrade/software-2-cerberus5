#https://blog.skyplabs.net/2018/03/01/python-sniffing-inside-a-thread-with-scapy/
from scapy.all import *
from threading import Thread, Event
from time import sleep
from netfilterqueue import NetfilterQueue
import datetime


class Sniffer(Thread):
	def __init__(self, filter_="", file__ = "snifferPcap.pcap", function = None):#interface="eth0",
		super().__init__()
		self.func = function
		self.daemon = True
		self.socket = None
		self.file_ = file__
		#self.interface = interface
		self.filter_ = filter_
		self.stop_sniffer = Event()
		self.nfqueue = NetfilterQueue()

	def run(self):
		""""now = datetime.datetime.now()
		file__ = str(now.strftime("%Y-%m-%d_%H.%M.%S"))+'.pcap'

		print(file__)"""
		open(self.file_, 'w').close()
		self.nfqueue.bind(1, self.modify_using_hooks)
		self.nfqueue.run()
		""""self.socket = conf.L2listen(
		type=ETH_P_ALL,
			#iface=self.interface,
			filter=self.filter_
		)"""

		#sniff(
		#	opened_socket=self.socket,
		#	prn=self.print_packet(file__) ,
		#	stop_filter=self.should_stop_sniffer
		#)

	def join(self, timeout=None):
		self.stop_sniffer.set()
		self.nfqueue.unbind()
		super().join(timeout)
	
	def modify_using_hooks(self, packet):
		pkt = IP(packet.get_payload())
		packet.drop()
		#modify packet		#send to enabled Hook Collections
		if not sniff(offline=pkt, filter=self.filter_):
			print("packet Denied")
			send(pkt)#############################
			return
		self.func(pkt)
		wrpcap(self.file_, pkt, append = True)
		print("packet Accepted")
		send(pkt)#############################
		return
	


	""""def should_stop_sniffer(self, packet):
		return self.stop_sniffer.isSet()"""

	""""def print_packet(self, file__ : str):
		print(file__ + 'file recieved\n')
		def appendToPcap(capturedPacket):
			print('Writing To PCAP' + file__)
			capturedPacket.show()
			#dissectPacket(capturedPacket)
			wrpcap(file__, capturedPacket, append = True)
		return appendToPcap"""

