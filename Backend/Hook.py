import os
import sys
import importlib

'''
Hook.py
author: Riley, Noah
'''
class Hook:

	def __init__(self, name, sequenceNumber, status, description):
		self.name = name
		self.sequenceNumber = sequenceNumber
		self.status = status
		self.description = description
		hookModule = importlib.import_module('hooks.{}'.format(name))
		hookClass = getattr(hookModule, name[0].upper() + name[1:])
		self.hook = hookClass()

	def hookInfo (self):
		print("Hook Name: " + self.name + "\n")
		print("Sequence Number: " + self.sequenceNumber + "\n")
		print("Status: " + self.status + "\n")
		print("Description: " + self.description + "\n")
		print("Path: " + self.path + "\n")
	
	def executeHook(self, packet):
		if self.status:
			self.hook.run(packet)
		
	def updateHookSequence(self, number):
		self.sequenceNumber = number
	
	def updateHookActivationState(self):
		self.status = not self.status
