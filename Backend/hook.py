import os
import sys

class hook:
	def __init__(self, name, sequenceNumber, status, description, path):
        self.name = name
        self.sequenceNumber = sequenceNumber
		self.status = status
		self.description = description
		self.path = path
	
	def hookInfo (self):
		print("Hook Name: " + self.name + "\n")
		print("Sequence Number: " + self.sequenceNumber + "\n")
		print("Status: " + self.status + "\n")
		print("Description: " + self.description + "\n")
		print("Path: " + self.path + "\n")
	
	def executeHook(self):
		os.system('python self.path');
		
	def updateHookSequence(self, number):
		self.sequenceNumber = number
	
	def updateHookActivationState(self):
		if self.status = true
			self.status = false
		    else:
			self.status = true
		
