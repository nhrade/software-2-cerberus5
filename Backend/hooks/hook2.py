
from scapy.all import *
import os

'''
hook2.py
@author Noah
changes source port of DNS packets to 44444
'''
class Hook2:

    def __init__(self):
        self.hookName = 'hook2'

    '''
    :returns modified packet:
    '''
    def run(self, packet):
        if DNS in packet:
            packet['UDP'].sport = 44444
        return packet
