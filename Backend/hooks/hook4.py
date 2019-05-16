'''
@author Noah
hook4.py
implements tcp handshake
'''

import random

class Hook4:

    def __init__(self):
        self.hookName = 'hook4'
        self.MAX_SEQ_NUM = 10000
        self.seqNum = random.randint(self.MAX_SEQ_NUM)

    def run(self, packet):
        ip = IP(src=packet['IP'].dst, dst=packet['IP'].src)
        if 'TCP' in packet and packet['TCP'].flags=='S':
            ack = TCP(sport=packet['TCP'].dport,
                      dport=packet['TCP'].sport,
                      flags='A', seq=self.seqNum,
                      ack=packet.seq + 1)
            send(ip/ack)
        return packet, False