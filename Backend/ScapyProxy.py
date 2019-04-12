#ScapyProxy
#Reference- https://www2.mmu.ac.uk/media/mmuacuk/content/documents/school-of-computing-mathematics-and-digital-technology/blossom/PythonScriptingwithScapyLab.pdf 


import scapy
from scapy.all import *

a=sniff(count=10)
a.nsummary()

send(IP(dst="184.0.0.0")/ICMP())
sendp(Ether()/IP(dst="184.0.0.0",ttl=(1,4)),iface="eth1")

ans,unans=sr(IP(dst="192.168.86.130",ttl=5)/ICMP())
ans.nsummary()
unans.nsummary()
p=sr1(IP(dst="192.168.86.130")/ICMP()/"XXXXXX")
p.show()
