import iptc

'''
hook3.py
@author Noah
Implements hook to drop all TCP packets
'''
class Hook3:

    def __init__(self):
        self.hookName = 'hook3'

    def run(self, packet):
        rule = iptc.Rule()
        rule.protocol = 'tcp'
        rule.create_target('DROP')
