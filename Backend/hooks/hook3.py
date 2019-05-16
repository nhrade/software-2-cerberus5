import iptc

'''
hook3.py
@author Noah
Implements hook to drop all TCP packets
'''
class Hook3:

    def __init__(self):
        self.hookName = 'hook3'

    '''
    :returns tuple of packet and whether to drop the packet or not:
    '''
    def run(self, packet):
        if 'TCP' in packet:
            return packet, True
        return packet, False

