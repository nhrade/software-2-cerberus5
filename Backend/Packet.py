#Sniffing packets, a go-go
#Reference - http://www.bitforestinfo.com/2017/01/how-to-write-simple-packet-sniffer.html

#Written to work with Linux
 
#import module
import socket
 
#create an INET, raw socket
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
 
# receive a packet
while True:

   # print output on terminal
   print s.recvfrom(65565)
   
def fields(data):
  storeobj=data
  storeobj=struct.unpack("!6s6sH",storeobj)
  destination_mac=binascii.hexlify(storeobj[0])
  source_mac=binascii.hexlify(storeobj[1])
  eth_protocol=storeobj[2]
  data={"Destination Mac":destination_mac,
  "Source Mac":source_mac,
  "Protocol":eth_protocol}
  return data
