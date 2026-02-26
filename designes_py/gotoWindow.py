from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 150)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 6, 345, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.goButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.goButton.setFont(font)
        self.goButton.setObjectName("goButton")
        self.horizontalLayout.addWidget(self.goButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 15)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.exitButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.horizontalLayout_3.setStretch(0, 20)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(216, 119, 143, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Go to:"))
        self.lineEdit.setToolTip(_translate("Dialog", "Find & Select"))
        self.goButton.setToolTip(_translate("Dialog", "Search line and select it"))
        self.goButton.setText(_translate("Dialog", "Go"))
        self.exitButton.setToolTip(_translate("Dialog", "Exit from go to window"))
        self.exitButton.setText(_translate("Dialog", "Exit"))

class GotoWindow(QtWidgets.QDialog):
    view = QtCore.pyqtSignal(tuple)

    def __init__(self, text: str):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.tr("Go to"))
        self.setFixedSize(self.size())
        self.text = text
        self.poses = []
        self._to_go = ""
        self._status = "Go"
        self._timer = QtCore.QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.setInterval(2000)
        self._timer.timeout.connect(self.ui.label_2.clear)
        self.show()

        self.ui.exitButton.clicked.connect(self.close)
        self.ui.goButton.clicked.connect(self.gotoHandler)

    def updateLabel(self, text: str):
        self.ui.label_2.setText(text)
        self._timer.start()

    def sendPos(self):
        text = self.ui.lineEdit.text().strip()
        if self._to_go != text:
            self._status = "Go"
            self._to_go = text
            self.gotoHandler()
            return
        elif not self.poses:
            QtWidgets.QMessageBox.critical(self, self.tr("Found error"), self.tr("Not found!"))
            self.updateLabel(self.tr("Not found!"))
            return
        pos = self.poses.pop(0)
        self.view.emit(pos)
        self.updateLabel(self.tr("Next"))

    def gotoHandler(self):
        if self._status == "Go":
            self.gotoText()
            self._status = "Next"
        elif self._status == "Next":
            self.sendPos()

    def gotoText(self):
        self.poses.clear()
        to_go = self.ui.lineEdit.text().strip()
        if not to_go:
            QtWidgets.QMessageBox.critical(self, self.tr("Text"), self.tr("You haven't written any letters!"))
            return
        elif to_go not in self.text:
            QtWidgets.QMessageBox.critical(self, self.tr("Found error"), self.tr("Not found!"))
            self.updateLabel(self.tr("Not found!"))
            return
        temp = -1
        while True:
            temp = self.text.find(to_go, temp + 1)
            if temp == -1:
                break
            pos = (temp, temp + len(to_go))
            self.poses.append(pos)
        self.sendPos()
        self.updateLabel(self.tr("Found!"))
