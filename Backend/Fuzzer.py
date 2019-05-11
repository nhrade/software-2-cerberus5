import os
import subprocess
import sys

'''
Fuzzer.py
Interface to AFL
author: Noah Hradek
'''
class Fuzzer:

    def __init__(self, afl_input, afl_output):
        self.afl_input = afl_input
        self.afl_output = afl_output

    def generateValue(self):
        buf = sys.stdin.read()
        print(buf)
        split = buf.split()
        subprocess.call(['/home/nhrade/.local/bin/py-afl-fuzz', '-i', self.afl_input,
                         '-o', self.afl_output, ' -- python FuzzingManager.py', '-d'])
        return (split[0], split[1])

