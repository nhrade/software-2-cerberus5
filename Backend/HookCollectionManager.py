import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

import Hook
import HookCollection

class HookCollectionManager(QtWidgets.MainWindow, QPushButton):

	hookCollectionList = []

	def __init__(self):
		super(MyWindow, self), __init__()
		uic.loadUi("HookCollectionView.ui", self)
		
		self.pushButton.clicked.connect(self.on_open1)
		self.pushButton_3.clicked.connect(self.on_open3)
		self.pushButton_2.clicked.connect(self.on_open1)
		self.pushButton_4.clicked.connect(self.on_open4)
		
		firstHookCollection = hookCollectionList[0]
		secondHookCollection = hookCollectionList[1]
		
		for h in firstHookCollection.listOfHooks:
			self.comboBox_21.addItem(h.name + ", " + h.description + ", " + h.path)
		
		for h in secondHookCollection.listOfHooks:
			self.comboBox_21.addItem(h.name + ", " + h.description + ", " + h.path)
		
		self.comboBox_21.clicked.connect(self.on_open21)
		self.comboBox_21.clicked.connect(self.on_open22)

	def on_open1(self):
		self.myOtherWindow = OtherWindow1()
		self.myOtherWindow = show();
		
	def on_open3(self):
		self.myOtherWindow = OtherWindow3()
		self.myOtherWindow = show();
	
	def on_open4(self):
		self.myOtherWindow = OtherWindow4()
		self.myOtherWindow = show();
	
	def on_open21(self):
		self.myOtherWindow = OtherWindow21()
		self.myOtherWindow = show();
	
	def on_open22(self):
		self.myOtherWindow = OtherWindow22()
		self.myOtherWindow = show();

class OtherWindow1(QtWidgets.QtMainWindow, QPushButton):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("CreateEditHookCollection.ui",self).show()
		
		self.statusComboBox.addItem("Enabled")
		self.statusComboBox.addItem("Disabled")
		self.saveButton.clicked.connect(self.clickMethod)
		self.cancelButton.clicked.connect(self.on_openHome)
	
	def clickMethod(self):
		selection = True
		if self.statusComboBox.currentText() == "Disabled":
			self.myOtherWindow = HookCollectionDisabled()
			self.myOtherWindow = show();
			selection = False
		hookC = HookCollection(self.hookCollectionNameEdit.text(), self.executionSequenceEdit.text(), selection, self.descriptionEdit.text(), 0, ListOfHooks = [])
		HookCollectionManager.hookCollectionList.append(hookC)
	
	def executionStatus(self):
		def __init__(self):
			super(OtherWindow,self),__init__()
			uic.loadUi("CreateEditHook.ui",self).show()

	def homeMethod(self):
		self.myOtherWindow = HookCollectionManager()
		self.myOtherWindow = show();
		
class OtherWindow3(QtWidgets.QtMainWindow, QPushButton):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("CreateEditHook.ui",self).show()
		
class HookCollectionDisabled(self):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("HookCollectionExecutionSequenceError.ui",self).show()
		
		self.saveButton.clicked.connect(self.backMethod)
		
	def backMethod(self):
		self.myOtherWindow = HookCollectionManager()
		self.myOtherWindow = show();
		
class HookView(self):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("HookView.ui",self).show()
		
		self.createHookButton.clicked.connect(self.createHook)

class createHook(self):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("CreateHook.ui",self).show()
		
		self.pushButton_2.clicked.connect(self.saveMethod)
		self.pushButton_3.clicked.connect(self.on_openHome)

	def clickMethod(self):
		thisHook = Hook(self.lineEdit.text(), 0, self.lineEdit_2.text(), True, lineEdit_3.text())
	

