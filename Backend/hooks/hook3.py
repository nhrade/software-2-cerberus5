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
    :returns packet or none if dropped:
    '''
    def run(self, packet):
        if 'TCP' in packet:
            return None
        return packet

