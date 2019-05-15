import os
import sys
import hook
import HookCollection
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

import hook
import HookCollection

class HookCollectionManager(QtWidgets.MainWindow, QPushButton):

	def __init__(self):
		super(MyWindow, self), __init__()
		uic.loadUi('HookCollectionView.ui", self)
		
		self.pushButton.clicked.connect(self.on_open1)
		self.pushButton_3.clicked.connect(self.on_open3)
		self.pushButton_2.clicked.connect(self.on_open1)
		self.pushButton_4.clicked.connect(self.on_open4)
		self.pushButton_45.clicked.connect(self.on_open45)
		self.pushButton_46.clicked.connect(self.on_open46)
		
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
	
	def on_open45(self):	
		self.myOtherWindow = OtherWindow45()
		self.myOtherWindow = show();
	
	def on_open46(self):
		self.myOtherWindow = OtherWindow46()
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
		uic.loadUi("CreateEditHook.ui",self).show()

class OtherWindow3(QtWidgets.QtMainWindow, QPushButton):
	def __init__(self):
		super(OtherWindow,self),__init__()
		uic.loadUi("CreateEditHook.ui",self).show()
	

