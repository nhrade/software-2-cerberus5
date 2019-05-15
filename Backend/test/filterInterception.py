#https://blog.skyplabs.net/2018/03/01/python-sniffing-inside-a-thread-with-scapy/
from scapy.all import *
from threading import Thread, Event
from time import sleep
from netfilterqueue import NetfilterQueue
import queue #interceptionQueue


class Interceptor(Thread):
	def __init__(self, filter_="", maxLength=100):#interface="eth0",
		super().__init__()
		
		self.daemon = True
		
		self.socket = None
		self.filter_ = filter_
		self.maxlength = maxLength
		self.stop_interception = Event()
		self.nfqueue = NetfilterQueue()
		self.internalQueue = queue.Queue(maxLength)#interceptionQueue.Intercepted()

	def run(self):
		#self.internalQueue = queue.Queue()
		#self.socket = conf.L2listen(
		#type=ETH_P_ALL,
			#iface=self.interface,
		#	filter=self.filter_)
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
		
		if not self.internalQueue.full():
			print("packet Accepted")
			self.internalQueue.put(pkt)#filterManager.interceptedQueue.push(pkt)
		return
	
	def forward(self, file_, num=1, internalQueue=None):
		print("At Forward")
		if internalQueue is not None:
			self.internalQueue = internalQueue
		print(self.internalQueue.empty())
		if self.internalQueue.qsize() >= num:
			for i in range(num):# and not self.internalQueue.empty():
				packet = self.internalQueue.get()
				print("At popped")
				packet.show()
				wrpcap(file_, packet, append = True)
				send(packet)
			print("After Pop")
		#self.internalQueue.pop(file_, numPacks)

	def dropPacket(self, num=1, internalQueue=None):
		print("At Drop")
		if internalQueue is not None:
			self.internalQueue = internalQueue
		if self.internalQueue.qsize() >= num:
			for i in range(num):# and not self.internalQueue.empty():
				packet = self.internalQueue.get()
				print("At popped")
				packet.show()
				#wrpcap(file_, packet, append = True)
				#send(packet)
			print("After Pop")
	
	def intercepted_packets(self):
		return self.internalQueue
		#return self.internalQueue.getQueue()
		
	def setIntercepted(queue_):
		self.internalQueue = queue_
		
