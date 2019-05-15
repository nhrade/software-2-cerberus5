import queue
from scapy.all import *

class Intercepted()
	def __init_(self)
		nf_queue_ = []
			
	def push(packet):

		self.nf_queue_.append(packet)
		
		
	def pop(file_, num=1):
		print("At Forward")
		for i in range(num):
			packet = self.nf_queue_.pop(0)
			print("At Forward")
			packet.show()
			wrpcap(file_, packet, append = True)
			send(packet)

	def getQueue():
		return nf_queue_
