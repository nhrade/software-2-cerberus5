#https://blog.skyplabs.net/2018/03/01/python-sniffing-inside-a-thread-with-scapy/
from scapy.all import *
from threading import Thread, Event
from time import sleep
from netfilterqueue import NetfilterQueue
import queue #interceptionQueue


class Interceptor(Thread):
	def __init__(self, filter_="", maxLength=100, queue_=[]):#interface="eth0",
		super().__init__()
		
		self.daemon = True
		
		#self.socket = None
		self.filter_ = filter_
		self.maxlength = maxLength
		self.stop_interception = Event()
		self.nfqueue = NetfilterQueue()

		self.internalQueue = []#queue.Queue(maxLength)#interceptionQueue.Intercepted()
		if queue_:
			self.internalQueue = queue_

	def run(self):
		#self.internalQueue = queue.Queue()
		#self.socket = conf.L2listen(
		#type=ETH_P_ALL,
			#iface=self.interface,
		#	filter=self.filter_)
		print(len(self.internalQueue))
		self.nfqueue.bind(0, self.modify_using_hooks, self.maxlength)
		self.nfqueue.run()
		


	def join(self, timeout=None):
		self.stop_interception.set()
		self.nfqueue.unbind()
		super().join(timeout)

	def modify_using_hooks(self, packet):
		pkt = IP(packet.get_payload())
		packet.drop()
		#modify packet
		# apply hooks
		if not sniff(offline=pkt, filter=self.filter_):
			print("packet Denied")
			send(pkt)
			return
		print(len(self.internalQueue))
		print(self.maxlength)
		if len(self.internalQueue) < self.maxlength:#.full():
			print("packet Accepted")
			self.internalQueue.append(pkt)#filterManager.interceptedQueue.push(pkt)
		return
	
	def forward(self, file_, packet):
		wrpcap(file_, packet, append = True)
		send(packet)
	

	def forward_packet(self, file_, num=1, internalQueue=[]):
		print(file_)
		print(num)
		print(len(internalQueue))
		print("At Forward")
		if internalQueue:
			print("recieved Packets")
			self.internalQueue = internalQueue
		print(len(self.internalQueue))
		if len(self.internalQueue) >= num:#.qsize() >= num:
			for i in range(num):# and not self.internalQueue.empty():
				packet = self.internalQueue.pop(0)
				print("At popped")
				packet.show()
				wrpcap(file_, packet, append = True)
				send(packet)
			print("After Pop")
		#self.internalQueue.pop(file_, numPacks)

	def dropPacket(self, num=1, internalQueue=[]):
		print("At Drop")
		if internalQueue:
			self.internalQueue = internalQueue
		if len(self.internalQueue) >= num:#.qsize() >= num:
			for i in range(num):# and not self.internalQueue.empty():
				packet = self.internalQueue.pop(0)
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
		
