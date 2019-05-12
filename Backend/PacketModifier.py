import sys
from scapy.all import sr1, IP, TCP


'''
PacketModifier.py
Interface to scapy/pypacker
author: Noah Hradek
'''
class PacketModifier:

    '''
    Create packet
    '''
    def modifyPacket(self, packet, values):
        p = IP(src=values['src_ip'], dst=values['dst_ip']) / TCP()
        return p