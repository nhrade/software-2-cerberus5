'''
hook2.py
@author Noah
'''
class Hook2:

    def __init__(self):
        self.hookName = 'hook2'

    '''
    :returns tuple of packet and whether to drop the packet or not:
    '''
    def run(self, packet):
        packet['DNS'].sport = 44444
        return packet, False