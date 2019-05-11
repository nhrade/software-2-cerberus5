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
