import webbrowser

from PyQt6 import QtCore, QtGui, QtWidgets

from .modules import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 4, 253, 203))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.autoSaveBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.autoSaveBox.setFont(font)
        self.autoSaveBox.setObjectName("autoSaveBox")
        self.verticalLayout.addWidget(self.autoSaveBox)
        self.numerationBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numerationBox.setFont(font)
        self.numerationBox.setObjectName("numerationBox")
        self.verticalLayout.addWidget(self.numerationBox)
        self.statusBarBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusBarBox.setFont(font)
        self.statusBarBox.setObjectName("statusBarBox")
        self.verticalLayout.addWidget(self.statusBarBox)
        self.backupFileBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backupFileBox.setFont(font)
        self.backupFileBox.setObjectName("backupFileBox")
        self.verticalLayout.addWidget(self.backupFileBox)
        self.qssStyleBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.qssStyleBox.setFont(font)
        self.qssStyleBox.setObjectName("qssStyleBox")
        self.verticalLayout.addWidget(self.qssStyleBox)
        self.clearBox = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearBox.setFont(font)
        self.clearBox.setObjectName("clearBox")
        self.verticalLayout.addWidget(self.clearBox)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(11, 367, 104, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(-1, 203, 266, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(262, -2, 5, 401))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(272, 2, 325, 389))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.applyButton = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.importButton = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_2.addWidget(self.importButton)
        self.resetButton = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.exitButton = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(6, 290, 137, 75))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.compileButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.compileButton.setObjectName("compileButton")
        self.verticalLayout_3.addWidget(self.compileButton)
        self.checkGithubButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.checkGithubButton.setObjectName("checkGithubButton")
        self.verticalLayout_3.addWidget(self.checkGithubButton)
        self.layoutWidget2 = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(6, 214, 227, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.autoSaveBox.setToolTip(_translate("Dialog", "Auto save changes"))
        self.autoSaveBox.setText(_translate("Dialog", "Auto save"))
        self.numerationBox.setToolTip(_translate("Dialog", "Enable / Disable numeration lines in file"))
        self.numerationBox.setText(_translate("Dialog", "Numeration"))
        self.statusBarBox.setToolTip(_translate("Dialog", "Enable / Disable statusbar"))
        self.statusBarBox.setText(_translate("Dialog", "StatusBar"))
        self.backupFileBox.setToolTip(_translate("Dialog", "Enable / Disable confirmation window"))
        self.backupFileBox.setText(_translate("Dialog", "Confirmation"))
        self.qssStyleBox.setToolTip(_translate("Dialog", "Enable / Disable black theme"))
        self.qssStyleBox.setText(_translate("Dialog", "QSS-styles"))
        self.clearBox.setToolTip(_translate("Dialog", "Enable / Disable cleaning text every n seconds"))
        self.clearBox.setText(_translate("Dialog", "Self-clear"))
        self.label_2.setText(_translate("Dialog", "Version: Unknown"))
        self.label_3.setText(_translate("Dialog", "Config"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here will be json-like settings</span></p></body></html>"))
        self.applyButton.setToolTip(_translate("Dialog", "Apply changes"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.importButton.setToolTip(_translate("Dialog", "Import config"))
        self.importButton.setText(_translate("Dialog", "Import"))
        self.resetButton.setToolTip(_translate("Dialog", "Resets config"))
        self.resetButton.setText(_translate("Dialog", "Reset"))
        self.exitButton.setToolTip(_translate("Dialog", "Exit from settings"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.compileButton.setToolTip(_translate("Dialog", "Compilation to exe"))
        self.compileButton.setText(_translate("Dialog", "Compile to exe"))
        self.checkGithubButton.setToolTip(_translate("Dialog", "Check this tool on github!"))
        self.checkGithubButton.setText(_translate("Dialog", "Visit Github"))
        self.label.setText(_translate("Dialog", "Auto-save seconds:"))
        self.label_4.setText(_translate("Dialog", "Self-clear seconds:"))

class SettingsWindow(QtWidgets.QDialog):
    changed = QtCore.pyqtSignal()
    settings_changed = QtCore.pyqtSignal()

    def __init__(self, version: str):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.tr("Settings"))
        self.setFixedSize(self.size())
        self.show()
        self._changed = False
        self._save_seconds = 0
        self._clear_seconds = 0

        self.ui.label_2.setText(self.tr("Version: {version}").format(version=version))
        self.settings = ""
        self.updateSettings()

        self.settings_template = {
            "File-numeration": self.ui.numerationBox,
            "StatusBar-info": self.ui.statusBarBox,
            "Self-clear": self.ui.clearBox,
            "Confirmation": self.ui.backupFileBox,
            "QSS-styles": self.ui.qssStyleBox,
            "Auto-save": self.ui.autoSaveBox,
            "Save_seconds": 0,
            "Clear_seconds": 0
        }

        self.checkSettings()
        self.updateVisualConfig()
        for box in tuple(self.settings_template.values())[:-2]:
            box.checkStateChanged.connect(self.change)

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.resetButton.clicked.connect(self.generateBasicSettings)
        self.ui.importButton.clicked.connect(self.importSettings)
        self.ui.applyButton.clicked.connect(self.applyChanges)

        self.ui.checkGithubButton.clicked.connect(lambda: webbrowser.open("https://github.com/qwert12201/QtNotepad", 2))
        self.ui.compileButton.clicked.connect(self.makeExeWrapper)

        self.changed.connect(self.checkSettings)
        self.ui.autoSaveBox.checkStateChanged.connect(lambda: self.ui.label.setEnabled(self.ui.autoSaveBox.isChecked()))
        self.ui.autoSaveBox.checkStateChanged.connect(lambda: self.ui.lineEdit.setEnabled(self.ui.autoSaveBox.isChecked()))
        self.ui.autoSaveBox.checkStateChanged.connect(self.ui.lineEdit.clear)

        self.ui.clearBox.checkStateChanged.connect(lambda: self.ui.label_4.setEnabled(self.ui.clearBox.isChecked()))
        self.ui.clearBox.checkStateChanged.connect(lambda: self.ui.lineEdit_2.setEnabled(self.ui.clearBox.isChecked()))
        self.ui.clearBox.checkStateChanged.connect(self.ui.lineEdit_2.clear)

    def makeExeWrapper(self):
        QtWidgets.QMessageBox.information(self, self.tr("Info"), self.tr("Building exe procces started!"))
        value = make_exe()
        if not value:
            QtWidgets.QMessageBox.critical(self, self.tr("Error"), self.tr("Building exe procces was interrupted and unsuccessful!"))
            return
        QtWidgets.QMessageBox.information(self, self.tr("Info"), self.tr("Building exe procces ended successful!\nYour result - main.exe in 'dist' folder."))

    def updateSettings(self):
        settings = get_settings()
        if not settings:
            settings = generate_basic_settings()
            updateFileConfig()
        self.settings = settings

    def change(self):
        self._changed = True

    def saveChanges(self) -> int:  # -1 - leave without save, 0 - not leave, 1 - leave with save
        self.updateSettings()
        if not self.settings["Confirmation"]:
            return -1
        elif self._changed:
            choice = QtWidgets.QMessageBox.question(self, self.tr("Warning"), self.tr("Do you want to save the changes?"), QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel, QtWidgets.QMessageBox.StandardButton.Save)
            if choice == QtWidgets.QMessageBox.StandardButton.Save:
                self.applyChanges()
                return 1
            elif choice == QtWidgets.QMessageBox.StandardButton.Cancel:
                return 0
            elif choice == QtWidgets.QMessageBox.StandardButton.No:
                return -1

    def getSeconds(self):
        a = self.ui.lineEdit.text()
        b = self.ui.lineEdit_2.text()
        if self.ui.lineEdit.isEnabled():
            if a.isdigit() and int(a) != 0:
                self._save_seconds = int(a)
            else:
                QtWidgets.QMessageBox.critical(self, self.tr("Incorrect seconds"), self.tr("Seconds aren't correctly!"))
                self._save_seconds = 0
        else:
            self._save_seconds = 0

        if self.ui.lineEdit_2.isEnabled():
            if b.isdigit() and int(b) != 0:
                self._clear_seconds = int(b)
            else:
                QtWidgets.QMessageBox.critical(self, self.tr("Incorrect seconds"), self.tr("Seconds aren't correctly!"))
                self._clear_seconds = 0
        else:
            self._clear_seconds = 0

    def closeEvent(self, a0):
        code = self.saveChanges()
        if code != 0:
            return super().closeEvent(a0)
        a0.ignore()

    def generateBasicSettings(self):
        self.settings = generate_basic_settings()
        updateFileConfig(self.settings)
        self.updateVisualConfig()
        self.ui.autoSaveBox.setChecked(False)
        self.ui.numerationBox.setChecked(False)
        self.ui.clearBox.setChecked(False)
        self.changed.emit()

    def importSettings(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open file"), filter="*.json")
        if file:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    settings = dict(json.load(f))
                    if settings.keys() != self.settings_template.keys():
                        QtWidgets.QMessageBox.critical(self, self.tr("Settings"), self.tr("Settings written incorrectly!"))
                        return
                    choice = QtWidgets.QMessageBox.warning(self, self.tr("Confirm"), self.tr("Do you confirm rewriting settings.json file?"), QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Cancel)
                    if choice == QtWidgets.QMessageBox.StandardButton.Cancel:
                        return
                    self.settings = settings
                    updateFileConfig(self.settings)
                    self.updateVisualConfig()
                    self.changed.emit()
                    self.settings_changed.emit()
            except json.JSONDecodeError:
                QtWidgets.QMessageBox.critical(self, self.tr("Settings"), self.tr("Settings in file isn't correctly!"))
                return

    def applyChanges(self):
        if self.settings.get("Confirmation"):
            choice = QtWidgets.QMessageBox.warning(self, self.tr("Confirm"), self.tr("Do you confirm rewriting settings.json file?"), QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Cancel)
            if choice == QtWidgets.QMessageBox.StandardButton.Cancel:
                return
        temp = {key: widget.isChecked() for key, widget in list(self.settings_template.items())[:-2]}
        self.getSeconds()
        if self._clear_seconds:
            temp["Clear_seconds"] = self._clear_seconds
        else:
            temp["Self-clear"] = False
            temp["Clear_seconds"] = 0

        if self._save_seconds:
            temp["Save_seconds"] = self._save_seconds
        else:
            temp["Auto-save"] = False
            temp["Save_seconds"] = 0
        self.settings = temp
        updateFileConfig(temp)
        self.updateVisualConfig()
        self.settings_changed.emit()
        self._changed = False

    def updateVisualConfig(self):
        settings = get_settings()
        result = "{\n"
        if settings:
            for key, value in settings.items():
                result += f"{' ' * 4}{key}: {value},\n"
            result += "}"
            self.ui.textEdit.setText(result)
        else:
            self.ui.textEdit.setText(self.tr("File not found!"))

    def checkSettings(self):
        for key, widget in list(self.settings_template.items())[:-2]:
            is_true = self.settings[key]
            widget.setChecked(is_true)
        if self.settings.get("Save_seconds"):
            self.ui.label.setEnabled(True)
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit.setText(str(self.settings["Save_seconds"]))
        if self.settings.get("Clear_seconds"):
            self.ui.label_4.setEnabled(True)
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.lineEdit_2.setText(str(self.settings["Clear_seconds"]))

    def exit(self):
        self.destroy(True)
