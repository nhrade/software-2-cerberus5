from PyQt5 import QtCore, QtGui, QtWidgets
from CreateEditHookDialog import Ui_CreateEditHook
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
from Hook import Hook

class Ui_HookView(object):
    def __init__(self):
        self.hookList = []

    def setupUi(self, HookView):
        HookView.setObjectName("HookView")
        HookView.resize(448, 338)
        self.gridLayout_3 = QtWidgets.QGridLayout(HookView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(HookView)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.searchEdit = QtWidgets.QLineEdit(HookView)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_3.addWidget(self.searchEdit, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.editHookButton = QtWidgets.QPushButton(HookView)
        self.editHookButton.setObjectName("editHookButton")
        self.gridLayout_2.addWidget(self.editHookButton, 0, 1, 1, 1)
        self.deleteHookButton = QtWidgets.QPushButton(HookView)
        self.deleteHookButton.setObjectName("deleteHookButton")
        self.gridLayout_2.addWidget(self.deleteHookButton, 0, 2, 1, 1)
        self.createHookButton = QtWidgets.QPushButton(HookView)
        self.createHookButton.setObjectName("createHookButton")
        self.gridLayout_2.addWidget(self.createHookButton, 0, 0, 1, 1)
        self.searchLabel = QtWidgets.QLabel(HookView)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout_2.addWidget(self.searchLabel, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.hookPropertiesFrame = QtWidgets.QFrame(HookView)
        self.hookPropertiesFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.hookPropertiesFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hookPropertiesFrame.setLineWidth(1)
        self.hookPropertiesFrame.setObjectName("hookPropertiesFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.hookPropertiesFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.hookPropertiesFrame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.hookPropertiesTable = QtWidgets.QTableWidget(self.hookPropertiesFrame)
        self.hookPropertiesTable.setObjectName("hookPropertiesTable")
        self.hookPropertiesTable.setColumnCount(3)
        self.hookPropertiesTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookPropertiesTable.setItem(0, 2, item)
        self.gridLayout_5.addWidget(self.hookPropertiesTable, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.hookPropertiesFrame, 1, 0, 1, 2)
        self.retranslateUi(HookView)
        QtCore.QMetaObject.connectSlotsByName(HookView)
        self.setupSignals()

    def setupSignals(self):
        self.createHookButton.clicked.connect(self.onCreateHook)

    def onCreateHook(self):
        self.createHookDialog = QtWidgets.QDialog()
        self.createHook = Ui_CreateEditHook(self)
        self.createHook.setupUi(self.createHookDialog)
        self.createHookDialog.show()

    def addHookToTable(self, hook):
        rowCount = self.hookPropertiesTable.rowCount()
        self.hookPropertiesTable.insertRow(rowCount)
        self.hookPropertiesTable.setItem(rowCount-1, 0, QtWidgets.QTableWidgetItem(hook.name))
        self.hookPropertiesTable.setItem(rowCount-1, 1, QtWidgets.QTableWidgetItem(hook.description))

    def updateHookView(self, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        path = kwargs['path']
        hook = Hook(name=name, sequenceNumber=self.hookPropertiesTable.rowCount(),
                                  status=True, description=description)
        self.hookList.append(hook)
        self.addHookToTable(hook)



    def retranslateUi(self, HookView):
        _translate = QtCore.QCoreApplication.translate
        HookView.setWindowTitle(_translate("HookView", "Form"))
        self.label_3.setText(_translate("HookView", "Page: 1 | 2 | 3"))
        self.editHookButton.setText(_translate("HookView", "Edit"))
        self.deleteHookButton.setText(_translate("HookView", "Delete"))
        self.createHookButton.setText(_translate("HookView", "+Hook"))
        self.searchLabel.setText(_translate("HookView", "Search"))
        self.label_2.setText(_translate("HookView", "Hook Properties"))
        item = self.hookPropertiesTable.verticalHeaderItem(0)
        item.setText(_translate("HookView", "*"))
        item = self.hookPropertiesTable.horizontalHeaderItem(0)
        item.setText(_translate("HookView", "Hook"))
        item = self.hookPropertiesTable.horizontalHeaderItem(1)
        item.setText(_translate("HookView", "Description"))
        item = self.hookPropertiesTable.horizontalHeaderItem(2)
        item.setText(_translate("HookView", "Association to Hook Collection"))
        __sortingEnabled = self.hookPropertiesTable.isSortingEnabled()
        self.hookPropertiesTable.setSortingEnabled(False)
        self.hookPropertiesTable.setSortingEnabled(__sortingEnabled)
