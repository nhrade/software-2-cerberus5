#https://blog.skyplabs.net/2018/03/01/python-sniffing-inside-a-thread-with-scapy/
from scapy.all import *
from threading import Thread, Event
from time import sleep
from netfilterqueue import NetfilterQueue
import filterManager


class Interceptor(Thread):
	def __init__(self, filter_="", maxLength=100):#interface="eth0",
		super().__init__()
		
		self.daemon = True
		self.filter_ = filter_
		self.maxlength = maxLength
		self.stop_interception = Event()
		self.nfqueue = NetfilterQueue()

	def run(self):
		self.nfqueue.bind(0, self.modify_using_hooks, self.maxlength)
		self.nfqueue.run()


	def join(self, timeout=None):
		self.stop_interception.set()
		super().join(timeout)

	def modify_using_hooks(self, packet):
		pkt = IP(packet.get_payload())
		packet.drop()
		#modify packet
		if not sniff(offline=pkt, filter=self.filter_):
			print("packet Denied")
			return
		print("packet Accepted")
		filterManager.interceptedQueue.push(pkt)
		return
