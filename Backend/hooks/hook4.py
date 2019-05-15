'''
@author Noah
hook4.py
implements tcp handshake
'''

class Hook4:

    def __init__(self):
        self.hookName = 'hook4'

    def run(self, packets):
        for packet in packets:
            if packet['TCP'] == 0:
