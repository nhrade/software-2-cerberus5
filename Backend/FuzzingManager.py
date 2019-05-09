'''
FuzzingManager.py
'''

from pypacker.layer3.ip import IP
from pypacker.layer3.icmp import ICMP

class FuzzingManager:

    def generateFuzzValue(self, field, vrange):
        pass

    def generateFuzzedPacket(self, packet, field, vrange, value):
        return IP(src_s="127.0.0.1", dst_s="192.168.0.1", p=1) + \
             ICMP(type=8) + \
             ICMP.Echo(id=123, seq=1, body_bytes=b"foobar")



fm = FuzzingManager()
ip = fm.generateFuzzedPacket(None, None, None, None)
print("%s" % ip)