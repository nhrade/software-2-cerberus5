import os
import sys
import Hook
'''
HookCollection.py
author: Riley
'''
class HookCollection:
	def __init__(self, name, sequenceNumber, status, description):
		self.name = name
		self.sequenceNumber = sequenceNumber
		self.status = status
		self.description = description
		self.associationCounter = 0
		self.listOfHooks = []
	
	def updateCollectionStatus(self):
		self.status = not self.status
			
	def addHookToList(self, thisHook):
		self.listOfHooks.append(thisHook)

	def editCollectionSequenceI(self, number):
		self.sequenceNumber = number
		
	def updateHookStatus(self):
		for hook in range(self.listOfHooks):
			hook.updateHookActivationState()
	
	def provideHookCollectionName(self):
		return self.name
	
	def searchForHook(self, thisHook):
		for h in range(self.listOfHooks):
			if h == thisHook:
				return h
	
	def executeHooks(self, packet):
		for hook in range(self.listOfHooks):
			hook.executeHook(packet)