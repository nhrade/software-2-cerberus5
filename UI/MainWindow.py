import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
from HookView import Ui_HookView
from HookCollectionView import Ui_HookCollectionView
from LivePacketView import Ui_LivePacketView
from PacketFromPCAPView import Ui_PacketFromPCAPView

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.optionView = QtWidgets.QFrame(self.centralwidget)
        self.optionView.setFrameShape(QtWidgets.QFrame.Panel)
        self.optionView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optionView.setObjectName("optionView")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.optionView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.optionView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hookOptionButton = QtWidgets.QPushButton(self.optionView)
        self.hookOptionButton.setObjectName("hookOptionButton")
        self.verticalLayout.addWidget(self.hookOptionButton)
        self.hookCollectionOptionButton = QtWidgets.QPushButton(self.optionView)
        self.hookCollectionOptionButton.setObjectName("hookCollectionOptionButton")
        self.verticalLayout.addWidget(self.hookCollectionOptionButton)
        self.livePacketOptionButton = QtWidgets.QPushButton(self.optionView)
        self.livePacketOptionButton.setObjectName("livePacketOptionButton")
        self.verticalLayout.addWidget(self.livePacketOptionButton)
        self.packetFromPCAPViewOptionButton = QtWidgets.QPushButton(self.optionView)
        self.packetFromPCAPViewOptionButton.setObjectName("packetFromPCAPViewOptionButton")
        self.verticalLayout.addWidget(self.packetFromPCAPViewOptionButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.optionView)
        self.contentView = QtWidgets.QFrame(self.centralwidget)
        self.contentView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentView.setObjectName("contentView")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.contentView)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedContentView = QtWidgets.QStackedWidget(self.contentView)
        self.stackedContentView.setObjectName("stackedContentView")

        self.hookView = Ui_HookView()
        self.hookViewWidget = QWidget()
        self.hookView.setupUi(self.hookViewWidget)

        self.hookCollectionView = Ui_HookCollectionView()
        self.hookCollectionViewWidget = QWidget()
        self.hookCollectionView.setupUi(self.hookCollectionViewWidget)

        self.livePacketView = Ui_LivePacketView()
        self.livePacketViewWidget = QWidget()
        self.livePacketView.setupUi(self.livePacketViewWidget)

        self.packetFromPCAPView = Ui_PacketFromPCAPView()
        self.packetFromPCAPViewWidget = QWidget()
        self.packetFromPCAPView.setupUi(self.packetFromPCAPViewWidget)

        self.stackedContentView.addWidget(self.hookViewWidget)
        self.stackedContentView.addWidget(self.hookCollectionViewWidget)
        self.stackedContentView.addWidget(self.livePacketViewWidget)
        self.stackedContentView.addWidget(self.packetFromPCAPViewWidget)

        self.horizontalLayout_3.addWidget(self.stackedContentView)
        self.horizontalLayout.addWidget(self.contentView)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExecution_Sequence_Error = QtWidgets.QAction(MainWindow)
        self.actionExecution_Sequence_Error.setObjectName("actionExecution_Sequence_Error")
        self.actionProxy_Behavior_Disabled = QtWidgets.QAction(MainWindow)
        self.actionProxy_Behavior_Disabled.setObjectName("actionProxy_Behavior_Disabled")
        self.actionQueue_Error_Message = QtWidgets.QAction(MainWindow)
        self.actionQueue_Error_Message.setObjectName("actionQueue_Error_Message")
        self.actionHook_Collection_Execution_Sequence_Error = QtWidgets.QAction(MainWindow)
        self.actionHook_Collection_Execution_Sequence_Error.setObjectName("actionHook_Collection_Execution_Sequence_Error")
        self.menuFile.addAction(self.actionExecution_Sequence_Error)
        self.menuFile.addAction(self.actionProxy_Behavior_Disabled)
        self.menuFile.addAction(self.actionQueue_Error_Message)
        self.menuFile.addAction(self.actionHook_Collection_Execution_Sequence_Error)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedContentView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeContentView(self, index):
        self.stackedContentView.setCurrentIndex(index)

    def setupSignals(self):
        self.hookOptionButton.clicked.connect(
            lambda: self.changeContentView(0))
        self.hookCollectionOptionButton.clicked.connect(
            lambda: self.changeContentView(1))
        self.livePacketOptionButton.clicked.connect(
            lambda: self.changeContentView(2))
        self.packetFromPCAPViewOptionButton.clicked.connect(
            lambda: self.changeContentView(3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Option View"))
        self.hookOptionButton.setText(_translate("MainWindow", "Hook"))
        self.hookCollectionOptionButton.setText(_translate("MainWindow", "Hook Collection"))
        self.livePacketOptionButton.setText(_translate("MainWindow", "Live Packet"))
        self.packetFromPCAPViewOptionButton.setText(_translate("MainWindow", "Packet from PCAP View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExecution_Sequence_Error.setText(_translate("MainWindow", "Hook Execution Sequence Error"))
        self.actionProxy_Behavior_Disabled.setText(_translate("MainWindow", "Proxy Behavior Disabled"))
        self.actionQueue_Error_Message.setText(_translate("MainWindow", "Queue Error Message"))
        self.actionHook_Collection_Execution_Sequence_Error.setText(_translate("MainWindow", "Hook Collection Execution Sequence Error"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    mainWindow = Ui_MainWindow()
    mainWindow.setupUi(window)
    mainWindow.setupSignals()
    window.show()
    sys.exit(app.exec_())