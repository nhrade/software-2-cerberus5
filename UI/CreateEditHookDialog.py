from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateEditHook(object):

    def __init__(self, hookView):
        self.hookView = hookView

    def setupUi(self, CreateEditHook):
        CreateEditHook.setObjectName("CreateEditHook")
        CreateEditHook.resize(372, 132)
        self.dialog = CreateEditHook
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(CreateEditHook)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 371, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.hookNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.hookNameEdit.setObjectName("hookNameEdit")
        self.horizontalLayout_2.addWidget(self.hookNameEdit)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.descriptionEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.horizontalLayout_4.addWidget(self.descriptionEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.hookPathEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.hookPathEdit.setObjectName("hookPathEdit")
        self.horizontalLayout_5.addWidget(self.hookPathEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.saveHookButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.saveHookButton.setObjectName("saveButton")
        self.horizontalLayout_6.addWidget(self.saveHookButton)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_6.addWidget(self.cancelButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.setupSignals()
        self.retranslateUi(CreateEditHook)
        QtCore.QMetaObject.connectSlotsByName(CreateEditHook)

    def saveHookButtonClicked(self):
        name = self.hookNameEdit.text()
        description = self.descriptionEdit.text()
        path = self.hookPathEdit.text()
        self.hookView.updateHookView(name=name, description=description, path=path)
        self.dialog.accept()

    def setupSignals(self):
        self.saveHookButton.clicked.connect(self.saveHookButtonClicked)

    def retranslateUi(self, CreateEditHook):
        _translate = QtCore.QCoreApplication.translate
        CreateEditHook.setWindowTitle(_translate("CreateEditHook", "Create/Edit Hook"))
        self.label.setText(_translate("CreateEditHook", "Hook Name"))
        self.label_2.setText(_translate("CreateEditHook", "Description"))
        self.label_3.setText(_translate("CreateEditHook", "Hook Path"))
        self.saveHookButton.setText(_translate("CreateEditHook", "Save"))
        self.cancelButton.setText(_translate("CreateEditHook", "Cancel"))
