#!/usr/bin/env python3
from scapySniffer import proxyOn
capture = False
while True:
	inp = input("input if capture \n")
	print(inp)
	if inp == "yes":
		capture = True
	else:
		capture = False
	print(capture)
	proxyOn(capture)
