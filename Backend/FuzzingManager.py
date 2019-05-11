from PacketModifier import *
from Fuzzer import *
from scapy.all import *
import sys
import afl

'''
FuzzingManager.py
Manages the fuzzing of packets and is external interface to other subsystems
'''
class FuzzingManager:

    def __init__(self):
        self.packetModifier = PacketModifier()
        self.fuzzer = Fuzzer('afl_input/', 'afl_output/')
        afl.init()

    def generateFuzzValue(self, field, vrange):
        v = self.fuzzer.generateValue()
        IP(dst=v[1], src=v[1])
        os._exit(0)

    def generateFuzzedPacket(self, packet, field, vrange, value):
        pass

if __name__ == '__main__':
    fm = FuzzingManager()
    fv = fm.generateFuzzValue('dst', (1, 10))
