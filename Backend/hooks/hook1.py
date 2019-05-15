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

    def run(self, packets):
        for packet in packets:
            packet['TCP'].sport = 55555