from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, threading
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Backend/test'))
import scapyUtilities, filterManager
#from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget

class Ui_LivePacketView(object):
    def setupUi(self, Form):
        self.pktsData = None
        self.packets = None
        self.likeWire = None
        self.inBinary = None
        self.inHex = None
        Form.setObjectName("Form")
        Form.resize(981, 842)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PcapFile = QtWidgets.QGroupBox(Form)
        self.PcapFile.setMaximumSize(QtCore.QSize(16777215, 80))
        self.PcapFile.setTitle("")
        self.PcapFile.setObjectName("ProxyBehavior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.PcapFile)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.PCAFile_2 = QtWidgets.QLabel(self.PcapFile)
        self.PCAFile_2.setObjectName("SnifferToggle")
        self.horizontalLayout_3.addWidget(self.PCAFile_2)
        self.ProxyDrop = QtWidgets.QComboBox(self.PcapFile)
        self.ProxyDrop.setObjectName("ProxyDrop")
        self.ProxyDrop.addItem("Disabled")
        self.ProxyDrop.addItem("Enabled")
        self.ProxyDrop.activated[str].connect(self.enabledProxy)
        self.horizontalLayout_3.addWidget(self.ProxyDrop)
        self.InterceptioLabel = QtWidgets.QLabel(self.PcapFile)
        self.InterceptioLabel.setObjectName("InterceptioLabel")
        self.horizontalLayout_3.addWidget(self.InterceptioLabel)
        self.InterceptionDrop = QtWidgets.QComboBox(self.PcapFile)
        self.InterceptionDrop.setObjectName("InterceptionDrop")
        self.InterceptionDrop.addItem("Disabled")
        self.InterceptionDrop.addItem("Enabled")
        self.InterceptionDrop.activated[str].connect(self.enabledInterceptor)
        self.horizontalLayout_3.addWidget(self.InterceptionDrop)
        self.QueueSizLabel = QtWidgets.QLabel(self.PcapFile)
        self.QueueSizLabel.setObjectName("QueueSizLabel")
        self.horizontalLayout_3.addWidget(self.QueueSizLabel)
        self.QueueSizeInput = QtWidgets.QPlainTextEdit(self.PcapFile)
        self.QueueSizeInput.setMaximumSize(QtCore.QSize(70, 16777215))
        self.QueueSizeInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QueueSizeInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.QueueSizeInput.setObjectName("QueueSizeInput")
        self.horizontalLayout_3.addWidget(self.QueueSizeInput)
        self.gridLayout.addWidget(self.PcapFile, 0, 0, 1, 1)
        self.PacketArea = QtWidgets.QGroupBox(Form)
        self.PacketArea.setMinimumSize(QtCore.QSize(0, 258))
        self.PacketArea.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.PacketArea.setObjectName("PacketArea")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.PacketArea)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 2, 1, 1)
        self.ClearButton_4 = QtWidgets.QPushButton(self.PacketArea)
        self.ClearButton_4.setObjectName("ClearButton_4")
        self.gridLayout_7.addWidget(self.ClearButton_4, 0, 1, 1, 1)
        self.PacketView_2 = QtWidgets.QTabWidget(self.PacketArea)
        self.PacketView_2.setObjectName("PacketView_2")
        self.Dissected_2 = QtWidgets.QWidget()
        self.Dissected_2.setObjectName("Dissected_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Dissected_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea = QtWidgets.QScrollArea(self.Dissected_2)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 769, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(769, 78))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        self.likeWire = self.treeWidget
        self.initializeTable(self.treeWidget, 10, 10)
        self.treeWidget.itemClicked.connect(self.populateFieldArea)

        self.gridLayout_19.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.PacketView_2.addTab(self.Dissected_2, "")
        self.Binary_2 = QtWidgets.QWidget()
        self.Binary_2.setObjectName("Binary_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.Binary_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Binary_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 755, 179))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.inBinary = self.treeWidget_2
        self.initializeTable(self.treeWidget_2, 10, 1)
        
        self.gridLayout_18.addWidget(self.treeWidget_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_12.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.PacketView_2.addTab(self.Binary_2, "")
        self.HEX_2 = QtWidgets.QWidget()
        self.HEX_2.setObjectName("HEX_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.HEX_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.HEX_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 755, 179))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_3)
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.inHex = self.treeWidget_3
        self.initializeTable(self.treeWidget_3, 10, 1)
        
        self.gridLayout_17.addWidget(self.treeWidget_3, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_13.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.PacketView_2.addTab(self.HEX_2, "")
        self.gridLayout_7.addWidget(self.PacketView_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.PacketArea, 2, 0, 1, 1)
        self.CapturFilterArea = QtWidgets.QGroupBox(Form)
        self.CapturFilterArea.setMaximumSize(QtCore.QSize(16777215, 80))
        self.CapturFilterArea.setObjectName("CapturFilterArea")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.CapturFilterArea)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.FilterLabel_2 = QtWidgets.QLabel(self.CapturFilterArea)
        self.FilterLabel_2.setObjectName("FilterLabel_2")
        self.gridLayout_5.addWidget(self.FilterLabel_2, 0, 0, 1, 1)
        self.FilterExpressionInput_2 = QtWidgets.QPlainTextEdit(self.CapturFilterArea)
        self.FilterExpressionInput_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.FilterExpressionInput_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.FilterExpressionInput_2.setObjectName("FilterExpressionInput_2")
        self.gridLayout_5.addWidget(self.FilterExpressionInput_2, 0, 1, 1, 1)
        self.ApplyButton_2 = QtWidgets.QPushButton(self.CapturFilterArea)
        self.ApplyButton_2.setObjectName("ApplyButton_2")
        self.gridLayout_5.addWidget(self.ApplyButton_2, 0, 2, 1, 1)
        self.ClearButton_3 = QtWidgets.QPushButton(self.CapturFilterArea)
        self.ClearButton_3.setObjectName("ClearButton_3")
        self.gridLayout_5.addWidget(self.ClearButton_3, 0, 3, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.CapturFilterArea, 1, 0, 1, 1)
        self.FieldandFuzzing = QtWidgets.QGroupBox(Form)
        self.FieldandFuzzing.setTitle("")
        self.FieldandFuzzing.setObjectName("FieldandFuzzing")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.FieldandFuzzing)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.FieldandFuzzing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Forward_2 = QtWidgets.QPushButton(self.groupBox)
        self.Forward_2.setObjectName("Forward_2")
        self.gridLayout_8.addWidget(self.Forward_2, 9, 2, 1, 1)
        self.SaveMod_2 = QtWidgets.QPushButton(self.groupBox)
        self.SaveMod_2.setObjectName("SaveMod_2")
        self.gridLayout_8.addWidget(self.SaveMod_2, 9, 1, 1, 1)
        self.Drop_2 = QtWidgets.QPushButton(self.groupBox)
        self.Drop_2.setObjectName("Drop_2")
        self.gridLayout_8.addWidget(self.Drop_2, 9, 3, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_8.addWidget(self.checkBox_10, 3, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_8, 1, 4, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_8.addWidget(self.checkBox_9, 4, 0, 1, 1)
        self.FieldValuesCol_2 = QtWidgets.QTreeWidget(self.groupBox)
        self.FieldValuesCol_2.setMinimumSize(QtCore.QSize(411, 192))
        self.FieldValuesCol_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.FieldValuesCol_2.setIndentation(10)
        self.FieldValuesCol_2.setUniformRowHeights(True)
        self.FieldValuesCol_2.setItemsExpandable(True)
        self.FieldValuesCol_2.setObjectName("FieldValuesCol_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.FieldValuesCol_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.FieldValuesCol_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.FieldValuesCol_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.FieldValuesCol_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.FieldValuesCol_2)
        self.gridLayout_8.addWidget(self.FieldValuesCol_2, 0, 1, 8, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 8, 1, 1, 2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setSizeIncrement(QtCore.QSize(0, 2))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_8.addWidget(self.checkBox_6, 5, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_8.addWidget(self.checkBox_7, 1, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_8.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_10, 2, 4, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_9, 4, 4, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_6, 3, 4, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_7, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 4, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 3, 0, 1, 1)
        self.FuzzingField = QtWidgets.QGroupBox(self.FieldandFuzzing)
        self.FuzzingField.setMinimumSize(QtCore.QSize(250, 0))
        self.FuzzingField.setObjectName("FuzzingField")
        self.SelectedPacketLabel_2 = QtWidgets.QLabel(self.FuzzingField)
        self.SelectedPacketLabel_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.SelectedPacketLabel_2.setObjectName("SelectedPacketLabel_2")
        self.SelectedPackeInput_2 = QtWidgets.QPlainTextEdit(self.FuzzingField)
        self.SelectedPackeInput_2.setGeometry(QtCore.QRect(140, 60, 141, 31))
        self.SelectedPackeInput_2.setObjectName("SelectedPackeInput_2")
        self.SelectedFieldName_2 = QtWidgets.QGroupBox(self.FuzzingField)
        self.SelectedFieldName_2.setGeometry(QtCore.QRect(10, 100, 271, 151))
        self.SelectedFieldName_2.setTitle("")
        self.SelectedFieldName_2.setObjectName("SelectedFieldName_2")
        self.SelectedField_2 = QtWidgets.QLabel(self.SelectedFieldName_2)
        self.SelectedField_2.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.SelectedField_2.setObjectName("SelectedField_2")
        self.ExpectedReturn_2 = QtWidgets.QLabel(self.SelectedFieldName_2)
        self.ExpectedReturn_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.ExpectedReturn_2.setObjectName("ExpectedReturn_2")
        self.Maximum_3 = QtWidgets.QLabel(self.SelectedFieldName_2)
        self.Maximum_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.Maximum_3.setObjectName("Maximum_3")
        self.Minimum_3 = QtWidgets.QLabel(self.SelectedFieldName_2)
        self.Minimum_3.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.Minimum_3.setObjectName("Minimum_3")
        self.Selected_2 = QtWidgets.QPlainTextEdit(self.SelectedFieldName_2)
        self.Selected_2.setGeometry(QtCore.QRect(130, 10, 141, 31))
        self.Selected_2.setObjectName("Selected_2")
        self.Expected_2 = QtWidgets.QPlainTextEdit(self.SelectedFieldName_2)
        self.Expected_2.setGeometry(QtCore.QRect(130, 40, 141, 31))
        self.Expected_2.setObjectName("Expected_2")
        self.Minimum_4 = QtWidgets.QPlainTextEdit(self.SelectedFieldName_2)
        self.Minimum_4.setGeometry(QtCore.QRect(130, 70, 141, 31))
        self.Minimum_4.setObjectName("Minimum_4")
        self.Maximum_4 = QtWidgets.QPlainTextEdit(self.SelectedFieldName_2)
        self.Maximum_4.setGeometry(QtCore.QRect(130, 100, 141, 31))
        self.Maximum_4.setObjectName("Maximum_4")
        self.Fuzz_2 = QtWidgets.QPushButton(self.FuzzingField)
        self.Fuzz_2.setGeometry(QtCore.QRect(100, 260, 75, 23))
        self.Fuzz_2.setObjectName("Fuzz_2")
        self.Stop_2 = QtWidgets.QPushButton(self.FuzzingField)
        self.Stop_2.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.Stop_2.setObjectName("Stop_2")
        self.gridLayout_9.addWidget(self.FuzzingField, 3, 3, 1, 1)
        self.Arrows = QtWidgets.QGroupBox(self.FieldandFuzzing)
        self.Arrows.setMaximumSize(QtCore.QSize(30, 100))
        self.Arrows.setTitle("")
        self.Arrows.setObjectName("Arrows")
        self.pushButton = QtWidgets.QPushButton(self.Arrows)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Arrows)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.Arrows, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.FieldandFuzzing, 3, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.PacketView_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PCAFile_2.setText(_translate("Form", "Proxy Behavior"))
        self.ProxyDrop.setItemText(0, _translate("Form", "Disabled"))
        self.ProxyDrop.setItemText(1, _translate("Form", "Enabled"))
        self.InterceptioLabel.setText(_translate("Form", "Interception Behavior"))
        self.InterceptionDrop.setItemText(0, _translate("Form", "Disabled"))
        self.InterceptionDrop.setItemText(1, _translate("Form", "Enabled"))
        self.QueueSizLabel.setText(_translate("Form", "Queue Size"))
        self.QueueSizeInput.setPlainText(_translate("Form", "Queue Size"))
        self.PacketArea.setTitle(_translate("Form", "Packet Area"))
        self.ClearButton_4.setText(_translate("Form", "Clear"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Dissected Packets"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        if self.pktsData ==None:
            self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "frame 249"))
            self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "DNS: query = utep.edu"))
            self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "frame 250"))
            self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "IP: src = 10.0.0.2"))
            self.treeWidget.setSortingEnabled(__sortingEnabled)
        else:
            for i, packet in enumerate(self.pktsData):
            #rootItem = QtWidgets.QTreeWidgetItem()
            #rootItem.setFlags(rootItem.flags() | QtCore.Qt.ItemIsEditable)
                l=list(scapyUtilities.dissectLayers(self.packets[i]))
                ":".join(str(l))
                self.treeWidget.topLevelItem(i).setText(0, 'frame %s: %s'%(i, str(l)))
            #print('frame %s: %s'%(i, str(l)))
            #rootItem.sceneSG={}
            #rootItem.sceneSG['code']='nextSceneFilename'
                for layer in packet:
                    #print(type(layer))
                    for j, (layername, layerInfo) in enumerate(layer.items()):
                        #childItem = QtWidgets.QTreeWidgetItem(rootItem)
                        #childItem.setFlags(rootItem.flags() | )
                        #childItem.sceneSG={}     
                        self.treeWidget.topLevelItem(i).child(j).setText(0, '%s: %s' %(layername, str(layerInfo)))
                        self.treeWidget.topLevelItem(i).child(j).setFlags(self.treeWidget.topLevelItem(i).flags() | QtCore.Qt.ItemIsEditable)

            #rootItem.setData(100, 77, QtCore.Qt.UserRole )
        
        self.PacketView_2.setTabText(self.PacketView_2.indexOf(self.Dissected_2), _translate("Form", "Dissected"))
        self.treeWidget_2.headerItem().setText(0, _translate("Form", "Binary Packets"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        if self.pktsData == None:
            self.treeWidget_2.topLevelItem(0).setText(0, _translate("Form", "frame 247"))
            self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("Form", "binary dump"))
            self.treeWidget_2.topLevelItem(1).setText(0, _translate("Form", "frame 248"))
            self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("Form", "binary dump"))
            self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        else:
            for i, packet in enumerate(self.pktsData):
            #rootItem = QtWidgets.QTreeWidgetItem()
            #rootItem.setFlags(rootItem.flags() | QtCore.Qt.ItemIsEditable)
                l=list(scapyUtilities.dissectLayers(self.packets[i]))
                ":".join(str(l))
                self.treeWidget_2.topLevelItem(i).setText(0, 'frame %s: %s'%(i, str(l)))
                self.treeWidget_2.topLevelItem(i).child(0).setText(0, str(scapyUtilities.binaryDump(self.packets[i])))


        self.PacketView_2.setTabText(self.PacketView_2.indexOf(self.Binary_2), _translate("Form", "Binary"))
        self.treeWidget_3.headerItem().setText(0, _translate("Form", "Hex Packets"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        if self.pktsData == None:
            self.treeWidget_3.topLevelItem(0).setText(0, _translate("Form", "frame 245"))
            self.treeWidget_3.topLevelItem(0).child(0).setText(0, _translate("Form", "hex dump"))
            self.treeWidget_3.topLevelItem(1).setText(0, _translate("Form", "frame 246"))
            self.treeWidget_3.topLevelItem(1).child(0).setText(0, _translate("Form", "hex dump"))
            self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        else:
            for i, packet in enumerate(self.pktsData):
            #rootItem = QtWidgets.QTreeWidgetItem()
            #rootItem.setFlags(rootItem.flags() | QtCore.Qt.ItemIsEditable)
                l=list(scapyUtilities.dissectLayers(self.packets[i]))
                ":".join(str(l))
                self.treeWidget_3.topLevelItem(i).setText(0, 'frame %s: %s'%(i, str(l)))
                self.treeWidget_3.topLevelItem(i).child(0).setText(0, str(scapyUtilities.hexDump(self.packets[i])))

        self.PacketView_2.setTabText(self.PacketView_2.indexOf(self.HEX_2), _translate("Form", "HEX"))
        self.CapturFilterArea.setTitle(_translate("Form", "Capture Filter"))
        self.FilterLabel_2.setText(_translate("Form", "Filter"))
        self.FilterExpressionInput_2.setPlainText(_translate("Form", "Filter Expression"))
        self.ApplyButton_2.setText(_translate("Form", "Apply"))
        self.ClearButton_3.setText(_translate("Form", "Clear"))
        self.pushButton.setText(_translate("Form", "|+>"))
        self.pushButton_2.setText(_translate("Form", "|+>"))
        self.FuzzingField.setTitle(_translate("Form", "Fuzzing Area"))
        self.SelectedPacketLabel_2.setText(_translate("Form", "Selected Packet Name"))
        self.SelectedPackeInput_2.setPlainText(_translate("Form", "Selected Packet Name"))
        self.SelectedField_2.setText(_translate("Form", "Selected Field Name"))
        self.Selected_2.setPlainText(_translate("Form", "Selected Field Name"))
        self.ExpectedReturn_2.setText(_translate("Form", "Expected Return Type"))
        self.Expected_2.setPlainText(_translate("Form", "Expected Return Type"))
        self.Minimum_3.setText(_translate("Form", "Minimum"))
        self.Minimum_4.setPlainText(_translate("Form", "Minimum"))
        self.Maximum_3.setText(_translate("Form", "Maximum"))
        self.Maximum_4.setPlainText(_translate("Form", "Maximum"))
        self.Fuzz_2.setText(_translate("Form", "Fuzz"))
        self.Stop_2.setText(_translate("Form", "Stop"))
        self.groupBox.setTitle(_translate("Form", "Field Area"))
        self.SaveMod_2.setText(_translate("Form", "Save Modification"))
        self.Drop_2.setText(_translate("Form", "Drop"))
        self.Forward_2.setText(_translate("Form", "Forward"))
        self.comboBox_8.setItemText(0, _translate("Form", "Format"))
        self.comboBox_8.setItemText(1, _translate("Form", "Dissected"))
        self.comboBox_8.setItemText(2, _translate("Form", "Hex"))
        self.comboBox_8.setItemText(3, _translate("Form", "Binary"))
        self.label.setText(_translate("Form", "Display Format"))
        self.label_2.setText(_translate("Form", "Field Name, value, and display format are editable fields"))
        self.FieldValuesCol_2.headerItem().setText(0, _translate("Form", "Field Name"))
        self.FieldValuesCol_2.headerItem().setText(1, _translate("Form", "Value"))
        self.FieldValuesCol_2.headerItem().setText(2, _translate("Form", "Mask"))
        __sortingEnabled = self.FieldValuesCol_2.isSortingEnabled()
        self.FieldValuesCol_2.setSortingEnabled(False)
        self.FieldValuesCol_2.topLevelItem(0).setText(0, _translate("Form", "icmp.type"))
        self.FieldValuesCol_2.topLevelItem(0).setText(1, _translate("Form", "08"))
        self.FieldValuesCol_2.topLevelItem(0).setText(2, _translate("Form", "0"))
        self.FieldValuesCol_2.topLevelItem(1).setText(0, _translate("Form", "icmp.code"))
        self.FieldValuesCol_2.topLevelItem(1).setText(1, _translate("Form", "00"))
        self.FieldValuesCol_2.topLevelItem(1).setText(2, _translate("Form", "0"))
        self.FieldValuesCol_2.topLevelItem(2).setText(0, _translate("Form", "icmp.checksum"))
        self.FieldValuesCol_2.topLevelItem(2).setText(1, _translate("Form", "6861"))
        self.FieldValuesCol_2.topLevelItem(2).setText(2, _translate("Form", "1"))
        self.FieldValuesCol_2.topLevelItem(3).setText(0, _translate("Form", "icmp.ident"))
        self.FieldValuesCol_2.topLevelItem(3).setText(1, _translate("Form", "809e"))
        self.FieldValuesCol_2.topLevelItem(3).setText(2, _translate("Form", "0"))
        self.FieldValuesCol_2.topLevelItem(4).setText(0, _translate("Form", "icmp.seq"))
        self.FieldValuesCol_2.topLevelItem(4).setText(1, _translate("Form", "0f00"))
        self.FieldValuesCol_2.topLevelItem(4).setText(2, _translate("Form", "2"))
        self.FieldValuesCol_2.setSortingEnabled(__sortingEnabled)

    """def openPCAP(self):
        pcap = self.PCAPLocation_2.toPlainText()
        self.packets, self.pktsData = scapyUtilities.unpackPCAP(pcap)
        print('Imported PCAP')
        self.retranslateUi(self.Form)"""

    def initializeTable(self, tree, items, subitems):
        for i in range(items):
            packet = self.addTreeSubItem(tree)
            for j in range(subitems):
                layer = self.addTreeSubItem(packet)
                #tree.clicked.connect(self.populateFieldArea(i, j))

    def enabledProxy(self, text):
        print("Proxy Enabled ")
        print(text)
        if str(text) is "Enabled":
            print("starting sniff thread")
            self.sniffThread = threading.Thread(target = scapyUtilities.toggleTheSniffer(), args=(self.addTreeItems,))
        else:
            
            scapyUtilities.toggleTheSniffer(False)

    def enabledInterceptor(self, text):
        print("Interceptor Enabled ")
        print(text)

    def addTreeItems(self, packet):
        print("adding items")
        
        

    def addTreeSubItem(self,parent):
        return QtWidgets.QTreeWidgetItem(parent)

    def populateFieldArea(self, layer):
        if self.pktsData is not None:
            packetRoot = layer.parent()
            if packetRoot is None:
                return
            treeRoot = packetRoot.parent()
            layerNum = packetRoot.indexOfChild(layer)

            try:
                for pac in range(self.treeWidget.topLevelItemCount()):
                    if self.treeWidget.topLevelItem(pac).text(0) == packetRoot.text(0):
                        packetNum = pac
                        break
                    else:
                        packetNum = 0
                print(packetNum, layerNum)
                print(self.pktsData[packetNum][layerNum])
 
            except:
                return
            #print(self.pktsData[packetNum][layerNum])
      

    def clearTables(self):
        self.clearTable(self.treeWidget)
        self.clearTable(self.treeWidget_2)
        self.clearTable(self.treeWidget_3)

    def clearTable(self, tree):
        for i in range(tree.topLevelItemCount()):
            tree.topLevelItem(i).setText(0,"")
            for j in range(tree.topLevelItem(i).childCount()):
                tree.topLevelItem(i).child(j).setText(0, "")

