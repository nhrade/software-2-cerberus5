from scapy.all import *
import os

'''
hook1.py
Change source of all TCP packets to 55555
@author noah
'''
class Hook1:

    def __init__(self):
        self.hookName = 'hook1'

    '''
    :returns tuple of packet and whether to drop the packet or not:
    '''
    def run(self, packet):
        packet['TCP'].sport = 55555
        return packet, False