from HookCollectionDialog import Ui_hookCollectionDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HookCollectionView(object):

    def __init__(self, hookCollectionManager):
        self.hookCollectionManager = hookCollectionManager

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(810, 293)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.createHookCollectionButton = QtWidgets.QPushButton(Form)
        self.createHookCollectionButton.setObjectName("createHookCollectionButton")
        self.horizontalLayout_3.addWidget(self.createHookCollectionButton)
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.editButton = QtWidgets.QPushButton(Form)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_3.addWidget(self.editButton)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.hookCollectionNameEdit = QtWidgets.QTextEdit(Form)
        self.hookCollectionNameEdit.setObjectName("hookCollectionNameEdit")
        self.gridLayout.addWidget(self.hookCollectionNameEdit, 1, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 2)
        self.hookCollectionTable = QtWidgets.QTableWidget(Form)
        self.hookCollectionTable.setObjectName("hookCollectionTable")
        self.hookCollectionTable.setColumnCount(4)
        self.hookCollectionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hookCollectionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookCollectionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookCollectionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hookCollectionTable.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.hookCollectionTable, 3, 2, 1, 3)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.createHookCollectionButton.clicked.connect(self.onCreateHookCollection)

    def onCreateHookCollection(self):
        self.createHookCollectionDialog = QtWidgets.QDialog()
        self.createHookCollection = Ui_hookCollectionDialog(self.hookCollectionManager, self)
        self.createHookCollection.setupUi(self.createHookCollectionDialog)
        self.createHookCollectionDialog.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_12.setText(_translate("Form", "Page: 1 | 2 | 3 ..."))
        self.createHookCollectionButton.setText(_translate("Form", "+Hook Collection"))
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.editButton.setText(_translate("Form", "Edit"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.hookCollectionNameEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#a1a1a1;\">Name of Hook Collection</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "Hook Collection Properties"))
        item = self.hookCollectionTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Hook Collection"))
        item = self.hookCollectionTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "No. Hooks"))
        item = self.hookCollectionTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Hook Collection Status"))
        item = self.hookCollectionTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Hook Collection Execution Sequence"))
