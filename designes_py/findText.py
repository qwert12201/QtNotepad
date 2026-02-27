from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setStyleSheet(
            "QDialog::QLabel {\n"
            "color: blue;\n"
            "}"
        )
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 170, 449, 125))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info1Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.info1Label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info1Label.setFont(font)
        self.info1Label.setObjectName("info1Label")
        self.verticalLayout.addWidget(self.info1Label)
        self.info2Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.info2Label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info2Label.setFont(font)
        self.info2Label.setObjectName("info2Label")
        self.verticalLayout.addWidget(self.info2Label)
        self.info3Label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.info3Label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info3Label.setFont(font)
        self.info3Label.setObjectName("info3Label")
        self.verticalLayout.addWidget(self.info3Label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previousButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.previousButton.setEnabled(False)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.nextButton.setEnabled(False)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 158, 453, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(62, 36, 257, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.showInfoBox = QtWidgets.QCheckBox(parent=Dialog)
        self.showInfoBox.setGeometry(QtCore.QRect(8, 140, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showInfoBox.setFont(font)
        self.showInfoBox.setObjectName("showInfoBox")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(331, -11, 2, 177))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.exitButton = QtWidgets.QPushButton(parent=Dialog)
        self.exitButton.setGeometry(QtCore.QRect(339, 135, 105, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.replaceModeButton = QtWidgets.QPushButton(parent=Dialog)
        self.replaceModeButton.setEnabled(False)
        self.replaceModeButton.setGeometry(QtCore.QRect(339, 95, 105, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replaceModeButton.setFont(font)
        self.replaceModeButton.setObjectName("replaceModeButton")
        self.resetReplaceButton = QtWidgets.QPushButton(parent=Dialog)
        self.resetReplaceButton.setEnabled(False)
        self.resetReplaceButton.setGeometry(QtCore.QRect(339, 65, 105, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.resetReplaceButton.setFont(font)
        self.resetReplaceButton.setObjectName("resetReplaceButton")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(2, 36, 55, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.clearButton = QtWidgets.QPushButton(parent=Dialog)
        self.clearButton.setGeometry(QtCore.QRect(339, 5, 105, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.saveMatchesButton = QtWidgets.QPushButton(parent=Dialog)
        self.saveMatchesButton.setEnabled(False)
        self.saveMatchesButton.setGeometry(QtCore.QRect(339, 35, 105, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.saveMatchesButton.setFont(font)
        self.saveMatchesButton.setObjectName("saveMatchesButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.info1Label.setText(_translate("Dialog", "Line to find: "))
        self.info2Label.setText(_translate("Dialog", "Total lines: "))
        self.info3Label.setText(_translate("Dialog", "Matches total: "))
        self.previousButton.setToolTip(_translate("Dialog", "Previous match"))
        self.previousButton.setText(_translate("Dialog", "Previous"))
        self.nextButton.setToolTip(_translate("Dialog", "Next match"))
        self.nextButton.setText(_translate("Dialog", "Next"))
        self.searchButton.setToolTip(_translate("Dialog", "Searches line in file"))
        self.searchButton.setText(_translate("Dialog", "Search"))
        self.showInfoBox.setToolTip(_translate("Dialog", "Get more info about matches"))
        self.showInfoBox.setText(_translate("Dialog", "Show info"))
        self.exitButton.setToolTip(_translate("Dialog", "Exit from search"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.replaceModeButton.setToolTip(_translate("Dialog", "Enable / Disable Replace text mode"))
        self.replaceModeButton.setText(_translate("Dialog", "ReplaceMode"))
        self.resetReplaceButton.setToolTip(_translate("Dialog", "Reset all replaces"))
        self.resetReplaceButton.setText(_translate("Dialog", "Reset replace"))
        self.label_2.setText(_translate("Dialog", "Find:"))
        self.clearButton.setToolTip(_translate("Dialog", "Clear all"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.saveMatchesButton.setToolTip(_translate("Dialog", "Save matches to file"))
        self.saveMatchesButton.setText(_translate("Dialog", "Save matches"))

class FindWindow(QtWidgets.QDialog):
    replace = QtCore.pyqtSignal()
    new_text = QtCore.pyqtSignal()

    def __init__(self, formatted_strings: list[str]):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.strings = formatted_strings
        self.buffer = []
        self.line_buffer = []
        self.index = 0
        self.to_find = ""
        self.replace_with = ""
        self.setWindowTitle(self.tr("Search"))
        self.show()

        self.info_widgets = [
            self.ui.info1Label, self.ui.info2Label, self.ui.info3Label,
        ]

        self.ui.replaceModeButton.clicked.connect(self.changeMode)
        self.ui.showInfoBox.checkStateChanged.connect(self.activateInfoLabels)
        self.ui.searchButton.clicked.connect(self.handleControlButton)
        self.ui.saveMatchesButton.clicked.connect(self.saveMatches)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.clearButton.clicked.connect(self.clearSearch)
        self.ui.resetReplaceButton.clicked.connect(lambda: self.ui.resetReplaceButton.setEnabled(False))

    def exit(self):
        self.destroy(True)

    def replaceStrings(self, new_lines: list[str]):
        self.strings = new_lines

    def changeMode(self):
        if not self.to_find:
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("You haven't searched any line!"))
            return
        self.ui.saveMatchesButton.setEnabled(False)
        self.ui.searchButton.setText(self.tr("Replace"))
        self.ui.label_2.setText(self.tr("Replace:"))
        self.ui.previousButton.setEnabled(False)
        self.ui.nextButton.setEnabled(False)
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setReadOnly(False)
        self.ui.replaceModeButton.setEnabled(False)
        self.ui.searchButton.setEnabled(True)

    def clearSearch(self):
        self.ui.lineEdit.clear()
        self.ui.showInfoBox.setEnabled(True)
        self.ui.showInfoBox.setChecked(False)
        self.ui.lineEdit.setReadOnly(False)
        self.ui.label_2.setText(self.tr("Find:"))
        self.ui.info1Label.setText(self.tr("Line to find: "))
        self.ui.info2Label.setText(self.tr("Total lines: "))
        self.ui.info3Label.setText(self.tr("Matches total: "))
        self.buffer.clear()
        self.line_buffer.clear()
        self.index = 0
        self.ui.nextButton.setEnabled(False)
        self.ui.previousButton.setEnabled(False)
        self.ui.saveMatchesButton.setEnabled(False)
        self.ui.replaceModeButton.setEnabled(False)
        self.ui.searchButton.setEnabled(True)
        self.ui.resetReplaceButton.setEnabled(False)
        self.ui.searchButton.setText(self.tr("Search"))
        self.new_text.emit()

    def activateInfoLabels(self):
        for widget in self.info_widgets:
            widget.setEnabled(self.ui.showInfoBox.isChecked())

    def updateInfo(self, to_find: str, total_lines: int, matches: int):
        info_labels_is_active = self.ui.info1Label.isEnabled()
        if info_labels_is_active:
            self.ui.info1Label.setText(self.tr('Line to find: "{to_find}"').format(to_find=to_find))
            self.ui.info2Label.setText(self.tr("Total lines: {total_lines}").format(total_lines=total_lines))
            self.ui.info3Label.setText(self.tr("Matches total: {matches}").format(matches=matches))

    def search(self):
        to_find = self.ui.lineEdit.text()
        if not to_find:
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("You haven't written any letters!"))
            return
        self.to_find = to_find
        matches, total_lines, temp = 0, 0, 0
        letters_iterated = 0
        for line in self.strings:
            line = line.strip()
            total_lines += 1
            if to_find in line:
                temp2 = 0
                while True:
                    temp = line.find(to_find, temp2)
                    if temp == -1:
                        break
                    temp2 = temp + 1
                    abs_pos = temp2 + letters_iterated - 1
                    res = (abs_pos, abs_pos + len(to_find))
                    self.buffer.append(res)
                    matches += 1
                self.line_buffer.append(line)
            letters_iterated += len(line) + 1
        self.updateInfo(to_find, total_lines, matches)

    def searchButton(self):
        self.search()
        if self.buffer or self.line_buffer:
            self.ui.lineEdit.setText(self.tr("Found!"))
            self.ui.previousButton.setEnabled(False)
            self.ui.nextButton.setEnabled(True)
            self.ui.saveMatchesButton.setEnabled(True)
            self.ui.replaceModeButton.setEnabled(True)
            self.ui.showInfoBox.setEnabled(False)
        else:
            self.ui.lineEdit.setText(self.tr("Not found!"))
        self.ui.lineEdit.setReadOnly(True)

    def replaceButton(self):
        self.replace_with = self.ui.lineEdit.text()
        if not self.replace_with:
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("You haven't written any letters!"))
            return
        self.replace.emit()
        self.ui.lineEdit.setReadOnly(True)
        self.ui.resetReplaceButton.setEnabled(True)

    def handleControlButton(self):
        button_text = self.ui.searchButton.text()
        if button_text == self.tr("Search"):
            self.searchButton()
        elif button_text == self.tr("Replace"):
            self.replaceButton()
        self.ui.searchButton.setEnabled(False)

    def saveMatches(self):
        if not self.buffer:
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("You have to search something to save!"))
            return
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, self.tr("Save file"))
        if not file:
            return
        try:
            with open(file, "w", encoding="utf-8") as f:
                for line in self.line_buffer:
                    f.write(line + "\n")
                QtWidgets.QMessageBox.information(self, self.tr("Success"), self.tr("Matches were saved!"))
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, self.tr("Permission error"), self.tr("You don't have permissions to write in file!"))
            return
