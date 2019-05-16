'''
@author Noah
hook4.py
implements tcp handshake
'''

import random
from scapy.all import *

class Hook4:

    def __init__(self):
        self.hookName = 'hook4'

    def run(self, packet):
        ip = IP(src=packet['IP'].dst, dst=packet['IP'].src)
        if 'TCP' in packet and packet['TCP'].flags=='S':
            ack = TCP(sport=packet['TCP'].dport,
                      dport=packet['TCP'].sport,
                      flags='A', seq=packet.seq + 1,
                      ack=packet.seq + 1)
            send(ip/ack)
        return packet

