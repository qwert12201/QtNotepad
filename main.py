import sys

from PyQt6 import QtWidgets, QtCore, QtGui

import resource  # noqa
from designes_py.modules import *  # noqa
from designes_py.design import Ui_MainWindow
from designes_py.findText import FindWindow
from designes_py.settingsWindow import SettingsWindow
from designes_py.gotoWindow import GotoWindow

class MainWindow(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.textEdit.clear()
        self.version = "1.3.4"
        self._lang = ""
        self.settings = {}
        self.context_menu = QtWidgets.QMenu(self)  # right click

        self.updateSettings()
        self.ui.statusBar.setVisible(self.settings["StatusBar-info"])
        self._numeration = self.settings["File-numeration"]
        self._save_seconds = self.settings["Save_seconds"]
        self._clear_seconds = self.settings["Clear_seconds"]

        # styles
        self.changeStyleMode(self.settings["QSS-styles"])
        self.show()

        self.colors = [
            "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gray", "White", "Black"
        ]

        self.format_table = {
            self.ui.actionBold: "Bold",
            self.ui.actionCrossOut: "CrossOut",
            self.ui.actionItalic: "Italic",
            self.ui.actionUnderline: "Underline",
            self.ui.actionResetFormat: "Reset"
        }

        self.weight_table = {
            self.ui.actionBold2: 700,
            self.ui.actionDemiBold: 600,
            self.ui.actionExtraBold: 800,
            self.ui.actionNormal: 400,
            self.ui.actionMedium: 500,
            self.ui.actionLight: 300,
            self.ui.actionThin: 100
        }

        self.file = None
        self.app_translator = QtCore.QTranslator(app)
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.timer.start())
        self.timer.timeout.connect(self._writeLines)
        self.timer_2 = QtCore.QTimer(self)
        self.timer_2.setSingleShot(True)
        self.timer_2.timeout.connect(lambda: self.timer_2.start())
        self.timer_2.timeout.connect(self.clearTextEdit)
        self.setTimers()
        self.ui.textEdit.cursorPositionChanged.connect(self.changeStatusBar)

        # menuFile
        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSave_as.triggered.connect(self.saveAsFile)
        self.ui.actionExit.triggered.connect(self.close)

        # menuEdit
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        for _clr in self.colors:
            temp_widget: QtGui.QAction = getattr(self.ui, "action" + _clr)
            temp_widget.triggered.connect(lambda _, clr=_clr: self.color(clr.lower()))
        self.ui.actionResetColor.triggered.connect(lambda: self.ui.textEdit.setTextColor(QtGui.QColor("white")))
        self.ui.actionReadOnly.triggered.connect(lambda: self.ui.textEdit.setReadOnly(not self.ui.textEdit.isReadOnly()))
        for widget, format in self.format_table.items():
            widget.triggered.connect(lambda _, fmt=format: self.formatingString(fmt))

        for action, weight in self.weight_table.items():
            action.triggered.connect(lambda _, w=weight: self.ui.textEdit.setFontWeight(w))
        self.ui.actionResetStyle.triggered.connect(self.resetStyles)

        # Feautures
        self.ui.menuFeatures.aboutToShow.connect(self.checkFeatures)
        self.ui.actionFind.triggered.connect(self.createFindWindow)
        self.ui.actionGoto.triggered.connect(self.createGotoWindow)
        self.ui.actionCaps.triggered.connect(lambda: self.textFo("Up"))
        self.ui.actionLower.triggered.connect(lambda: self.textFo("Down"))

        # ContextMenu right click
        self.ui.actionDelete.triggered.connect(lambda: self.ui.textEdit.textCursor().removeSelectedText())
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.context_menu.addActions([
            self.ui.actionUndo,
            self.ui.actionRedo,
        ])
        self.context_menu.addSeparator()
        self.context_menu.addActions([
            self.ui.actionDelete,
            self.ui.actionCopy,
            self.ui.actionPaste,
            self.ui.actionCut,
        ])
        self.context_menu.addSeparator()
        self.context_menu.addMenu(self.ui.menuColor)
        self.context_menu.addMenu(self.ui.menuText_view)
        self.context_menu.addSeparator()
        self.context_menu.addAction(self.ui.actionResetStyle)
        self.ui.textEdit.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.textEdit.customContextMenuRequested.connect(self.showContextMenuEvent)

        # Settings
        self.ui.actionMenu.triggered.connect(self.createSettingsWindow)
        self.ui.actionReset_settings.triggered.connect(lambda: updateFileConfig(generate_basic_settings()))
        self.ui.actionAbout.triggered.connect(lambda: QtWidgets.QMessageBox.about(self, self.tr("About"), self.tr("Thank you for using my project!\n\nI try to make all my tools without AI, so notepad can contains errors and mistakes. If you find some of them, then please make a pull request or report them in 'Issues' tab in github")))
        self.ui.actionRussian.triggered.connect(lambda: self.translation("ru"))
        self.ui.actionEnglish.triggered.connect(lambda: self.translation("eng"))

    def textFo(self, mode: str):
        cursor = self.ui.textEdit.textCursor()
        cursor.insertText(cursor.selectedText().upper() if mode == "Up" else cursor.selectedText().lower())
        self.ui.textEdit.setTextCursor(cursor)

    def checkFeatures(self):
        text = self.ui.textEdit.toPlainText().strip()
        cursor = self.ui.textEdit.textCursor()
        self.ui.actionFind.setEnabled(len(text) > 0)
        self.ui.actionGoto.setEnabled(len(text) > 0)
        self.ui.actionCaps.setEnabled(cursor.hasSelection())
        self.ui.actionLower.setEnabled(cursor.hasSelection())

    def translation(self, lang: str):
        app.removeTranslator(self.app_translator)
        self.app_translator.load(f"{path}translations\\{lang}.qm")
        app.installTranslator(self.app_translator)
        self._lang = lang
        self.ui.retranslateUi(self)

    def updateSettings(self):
        settings = get_settings()
        if not settings:
            settings = generate_basic_settings()
            updateFileConfig(settings)
        self.settings = settings

    def changeStatusBar(self):
        self.updateSettings()
        setting = self.settings["StatusBar-info"]
        self.ui.statusBar.setVisible(setting)
        if setting:
            cursor = self.ui.textEdit.textCursor()
            first = cursor.position()
            second = cursor.columnNumber()
            third = cursor.blockNumber()
            self.ui.statusBar.showMessage(self.tr("Current cursor position: {first}, line: {third}, column: {second}").format(first=first, third=third, second=second))

    def showContextMenuEvent(self, pos):
        self.context_menu.exec(self.ui.textEdit.viewport().mapToGlobal(pos))

    def closeEvent(self, a0):
        code = self.saveChanges()
        if code == 1:
            self.closed.emit()
            return super().closeEvent(a0)
        a0.ignore()

    def _fileSaver(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, self.tr("Save file"))
        if file:
            self.file = file

    def _writeLines(self):
        if not self._save_seconds:
            self.timer.stop()
        if self.file:
            try:
                with open(self.file, "w", encoding="utf-8") as f:
                    text = self.ui.textEdit.toPlainText().split("\n")
                    for i, line in enumerate(text, start=1):
                        if self._numeration:
                            if line.strip():
                                line = str(i) + " " + line
                        line += "\n"
                        f.write(line)
            except PermissionError:
                QtWidgets.QMessageBox.critical(self, self.tr("Permissions"), self.tr("You don't have rights to apply changes!"))

    def clearTextEdit(self):
        if not self._clear_seconds:
            self.timer_2.stop()
        self.ui.textEdit.clear()

    def saveChanges(self) -> int:  # 0 - not leave, 1 - leave
        self.updateSettings()
        if not self.settings["Confirmation"]:
            return 1
        elif self.ui.textEdit.toPlainText():
            choice = QtWidgets.QMessageBox.question(self, self.tr("Warning"), self.tr("Do you want to save the changes?"), QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel, QtWidgets.QMessageBox.StandardButton.Save)
            if choice == QtWidgets.QMessageBox.StandardButton.Save:
                if not self.file:
                    self._fileSaver()
                self._writeLines()
            elif choice == QtWidgets.QMessageBox.StandardButton.Cancel:
                return 0
        return 1

    def newFile(self):
        code = self.saveChanges()
        if code != 0:
            self.ui.textEdit.clear()

    def openFile(self):
        code = self.saveChanges()
        if code == 0:
            return
        elif code == 1:
            self._writeLines()
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open file"), filter="*.txt")
        if file:
            self.file = file
            self.ui.textEdit.clear()
            try:
                with open(self.file, "r", encoding="utf-8") as f:
                    for line in f:
                        self.ui.textEdit.append(line[:-1])
            except UnicodeError:
                QtWidgets.QMessageBox.critical(self, self.tr("Unicode Error"), self.tr("File contains non utf-8 symbols and can't be viewed!"))

    def saveFile(self):
        if not self.file:
            self._fileSaver()
        self._writeLines()

    def saveAsFile(self):
        self._fileSaver()
        self._writeLines()

    def color(self, clr: str):
        text_cursor = self.ui.textEdit.textCursor()
        temp_clr = QtGui.QColor(clr)
        if not self.ui.textEdit.toPlainText():
            return
        self.ui.textEdit.setTextColor(temp_clr)
        text_cursor.clearSelection()

    def formatingString(self, tformat_action: str):
        text_cursor = self.ui.textEdit.textCursor()
        format = QtGui.QTextCharFormat()
        if not self.ui.textEdit.toPlainText():
            return

        if tformat_action == "Bold":
            format.setFontWeight(700 if text_cursor.charFormat().fontWeight() != 700 else 400)

        elif tformat_action == "CrossOut":
            format.setFontStrikeOut(not text_cursor.charFormat().fontStrikeOut())

        elif tformat_action == "Italic":
            format.setFontItalic(not text_cursor.charFormat().fontItalic())

        elif tformat_action == "Underline":
            format.setFontUnderline(not text_cursor.charFormat().fontUnderline())

        elif tformat_action == "Reset":
            temp = QtGui.QTextCharFormat()
            temp.setFontWeight(400)
            temp.setFontStrikeOut(False)
            temp.setFontItalic(False)
            temp.setFontUnderline(False)
            text_cursor.setCharFormat(temp)
            return

        self.ui.textEdit.mergeCurrentCharFormat(format)

    def resetStyles(self):
        self.ui.textEdit.setTextColor(QtGui.QColor("white"))
        text_cursor = self.ui.textEdit.textCursor()
        temp = QtGui.QTextCharFormat()
        temp.setFontWeight(400)
        temp.setFontStrikeOut(False)
        temp.setFontItalic(False)
        temp.setFontUnderline(False)
        text_cursor.setCharFormat(temp)

    def replaceText(self, to_replace: str, replace_with: str, mode: int):
        # 1 - replace, 0 - return old
        text = self.ui.textEdit.toPlainText()
        if mode == 1:
            text = text.replace(to_replace, replace_with)
        else:
            text = text.replace(replace_with, to_replace)
        self.ui.textEdit.setText(text)

    def resetSelection(self):
        a = self.ui.textEdit.textCursor()
        a.clearSelection()
        self.ui.textEdit.setTextCursor(a)

    def viewText(self, window: QtWidgets.QDialog, mode: int):
        self.resetSelection()
        if not window.buffer:
            return
        try:
            cursor = self.ui.textEdit.textCursor()
            if mode == 1:
                cursor.setPosition(window.buffer[window.index][1], QtGui.QTextCursor.MoveMode.MoveAnchor)
                cursor.setPosition(window.buffer[window.index][0], QtGui.QTextCursor.MoveMode.KeepAnchor)
                if not window.index + 1 >= len(window.buffer):
                    window.index += 1
                else:
                    window.ui.nextButton.setEnabled(False)
                window.ui.previousButton.setEnabled(True)
            elif mode == 0:
                cursor.setPosition(window.buffer[window.index][0], QtGui.QTextCursor.MoveMode.MoveAnchor)
                cursor.setPosition(window.buffer[window.index][1], QtGui.QTextCursor.MoveMode.KeepAnchor)
                if not window.index - 1 < 0:
                    window.index -= 1
                else:
                    window.ui.previousButton.setEnabled(False)
                window.ui.nextButton.setEnabled(True)
            self.ui.textEdit.setTextCursor(cursor)
        except IndexError:
            cursor.setPosition(0, QtGui.QTextCursor.MoveMode.MoveAnchor)
            window.ui.nextButton.setEnabled(False)
            window.ui.previousButton.setEnabled(True)
            return

    def getLines(self) -> list[str] | None:
        text = self.ui.textEdit.toPlainText()
        text = text.replace("\t", "    ")
        self.ui.textEdit.setText(text)
        if not text:
            return
        text = text.split("\n")
        result = []
        for t in text:
            result.extend(t.split(" "))
        return result

    def changeStyleModeSettingsWindow(self, window: QtWidgets.QDialog, enabled: bool):
        if enabled:
            window.setStyleSheet(multiply_parser("QDialog", "QLabel", "QPushButton", "QCheckBox", "QLineEdit", "QToolTip"))
            window.ui.textEdit.setStyleSheet(parse_qss("QTextEdit"))
        else:
            window.setStyleSheet("")
            window.ui.textEdit.setStyleSheet("")

    def changeStyleModeFindWindow(self, window: QtWidgets.QDialog, enabled: bool):
        if enabled:
            window.setStyleSheet(multiply_parser("QDialog", "QLabel", "QPushButton", "QToolTip"))
            window.ui.lineEdit.setStyleSheet(parse_qss("QLineEdit"))
            window.ui.showInfoBox.setStyleSheet(parse_qss("QCheckBox"))
            window.ui.verticalLayoutWidget.setStyleSheet("QLabel {font-size: 11pt;}")

    def changeStyleModeGotoWindow(self, window: QtWidgets.QDialog, enabled: bool):
        if enabled:
            window.setStyleSheet(multiply_parser("QDialog", "QLabel", "QPushButton", "QToolTip"))
            window.ui.lineEdit.setStyleSheet(parse_qss("QLineEdit"))

    def changeStyleMode(self, enabled: bool):
        if enabled:
            self.setStyleSheet(multiply_parser("QDialog", "QPushButton", "QLabel"))
            self.ui.centralwidget.setStyleSheet("background-color: #4c4c4c;")
            self.ui.menubar.setStyleSheet(parse_qss("QMenuBar") + "\n\n" + parse_qss("QMenu"))
            self.ui.textEdit.setStyleSheet(parse_qss("QScrollBar") + "\n\n" + parse_qss("QTextEdit"))
            self.ui.statusBar.setStyleSheet(parse_qss("QStatusBar"))
            self.context_menu.setStyleSheet(parse_qss("QMenu"))
        else:
            self.setStyleSheet("")
            self.ui.centralwidget.setStyleSheet("")
            self.ui.menubar.setStyleSheet("")
            self.ui.textEdit.setStyleSheet("")
            self.ui.statusBar.setStyleSheet("")
            self.context_menu.setStyleSheet("")

    def setTimers(self):
        if self._save_seconds:
            self.timer.setInterval(self._save_seconds * 1000)
            self.timer.start()
        if self._clear_seconds:
            self.timer_2.setInterval(self._clear_seconds * 1000)
            self.timer_2.start()

    def viewHandler(self, pos: tuple[int, int]):
        self.resetSelection()
        cursor = self.ui.textEdit.textCursor()
        cursor.setPosition(pos[0], QtGui.QTextCursor.MoveMode.MoveAnchor)
        cursor.setPosition(pos[1], QtGui.QTextCursor.MoveMode.KeepAnchor)
        self.ui.textEdit.setTextCursor(cursor)

    def signalHandler(self, window: QtWidgets.QDialog):
        settings = get_settings()
        if not settings:
            return
        self.changeStyleMode(settings["QSS-styles"])
        self.changeStyleModeSettingsWindow(window, settings["QSS-styles"])
        self._numeration = settings["File-numeration"]
        self._save_seconds = settings.get("Save_seconds")
        self._clear_seconds = settings.get("Clear_seconds")
        self.setTimers()

    def createGotoWindow(self):
        text = self.ui.textEdit.toPlainText()
        self.updateSettings()
        window = GotoWindow(text)
        self.changeStyleModeGotoWindow(window, self.settings["QSS-styles"])
        self.closed.connect(window.close)
        window.view.connect(self.viewHandler)
        window.exec()

    def createSettingsWindow(self):
        self.updateSettings()
        window = SettingsWindow(self.version)
        if self._lang == "ru":
            font = QtGui.QFont()
            font.setPointSize(8)
            window.ui.compileButton.setFont(font)
            window.ui.checkGithubButton.setFont(font)
            window.ui.importButton.setFont(font)
            window.ui.resetButton.setFont(font)
            window.ui.applyButton.setFont(font)
            window.ui.exitButton.setFont(font)
            window.ui.applyButton.setStyleSheet("min-width: 45px;")
            window.ui.importButton.setStyleSheet("min-width: 45px;")
        self.changeStyleModeSettingsWindow(window, self.settings["QSS-styles"])
        window.settings_changed.connect(lambda: self.signalHandler(window))
        self.closed.connect(window.exit)
        window.exec()

    def createFindWindow(self):
        text = self.getLines()
        self.updateSettings()
        window = FindWindow(text)
        self.changeStyleModeFindWindow(window, self.settings["QSS-styles"])
        if self._lang == "ru":
            window.ui.label_2.setStyleSheet("font-size: 8pt;")
        window.ui.previousButton.clicked.connect(lambda: self.viewText(window, 0))
        window.ui.nextButton.clicked.connect(lambda: self.viewText(window, 1))
        window.ui.resetReplaceButton.clicked.connect(lambda: self.replaceText(window.to_find, window.replace_with, 0))
        self.closed.connect(window.exit)
        window.replace.connect(lambda: self.replaceText(window.to_find, window.replace_with, 1))
        window.new_text.connect(lambda: window.replaceStrings(self.getLines()))
        window.exec()
        cursor = self.ui.textEdit.textCursor()
        cursor.setPosition(0, QtGui.QTextCursor.MoveMode.MoveAnchor)
        self.ui.textEdit.setTextCursor(cursor)
        self.resetSelection()


if __name__ == '__main__':
    future()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())
