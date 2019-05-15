'''
hook3.py
@author Noah
Implements hook to drop all TCP packets
'''
class Hook3:

    def __init__(self):
        self.hookName = 'hook3'

    def run(self, packets):
        for packet in packets:
            if 'TCP' in packet:
                packets.remove(packet)
