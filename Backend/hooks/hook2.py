'''
hook2.py
@author Noah
'''
class Hook2:

    def __init__(self):
        self.hookName = 'hook2'

    def run(self, packets):
        for packet in packets:
            packet['DNS'].sport = 44444
