#https://blog.skyplabs.net/2018/03/01/python-sniffing-inside-a-thread-with-scapy/
from scapy.all import *
from threading import Thread, Event
from time import sleep
import datetime


class Sniffer(Thread):
	def __init__(self, filter_=""):#interface="eth0",
		super().__init__()

		self.daemon = True
		self.socket = None
		#self.interface = interface
		self.filter_ = filter_
		self.stop_sniffer = Event()

	def run(self):
		now = datetime.datetime.now()
		file__ = str(now.strftime("%Y-%m-%d_%H.%M.%S"))+'.pcap'
		open(file__, 'w').close
		print(file__)
		self.socket = conf.L2listen(
		type=ETH_P_ALL,
			#iface=self.interface,
			filter=self.filter_
		)

		sniff(
			opened_socket=self.socket,
			prn=self.print_packet(file__) ,
			stop_filter=self.should_stop_sniffer
		)

	def join(self, timeout=None):
		self.stop_sniffer.set()
		super().join(timeout)
	
	def should_stop_sniffer(self, packet):
		return self.stop_sniffer.isSet()

	def print_packet(self, file__ : str):
		print(file__ + 'file recieved\n')
		def appendToPcap(capturedPacket):
			print('Writing To PCAP' + file__)
			capturedPacket.show()
			wrpcap(file__, capturedPacket, append = True)
		return appendToPcap

