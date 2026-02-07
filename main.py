import sys

from PyQt6 import QtWidgets, QtCore, QtGui

from modules import *
from designes_py.design import Ui_MainWindow
from designes_py.findText import Ui_Dialog as FindDialog

class FindWindow(QtWidgets.QDialog):
    replace = QtCore.pyqtSignal()
    new_text = QtCore.pyqtSignal()

    def __init__(self, formatted_strings: list[str]):
        super().__init__()
        self.ui = FindDialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.strings = formatted_strings
        self.buffer = []
        self.line_buffer = []
        self.index = 0
        self.to_find = ""
        self.replace_with = ""
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
            QtWidgets.QMessageBox.critical(self, "Error", "You haven't searched any line!")
            return
        self.ui.saveMatchesButton.setEnabled(False)
        self.ui.searchButton.setText("Replace")
        self.ui.label_2.setText("Replace:")
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
        self.ui.label_2.setText("Find:")
        self.ui.info1Label.setText("Line to find: ")
        self.ui.info2Label.setText("Total lines: ")
        self.ui.info3Label.setText("Matches total: ")
        self.buffer.clear()
        self.line_buffer.clear()
        self.index = 0
        self.ui.nextButton.setEnabled(False)
        self.ui.previousButton.setEnabled(False)
        self.ui.saveMatchesButton.setEnabled(False)
        self.ui.replaceModeButton.setEnabled(False)
        self.ui.searchButton.setEnabled(True)
        self.ui.resetReplaceButton.setEnabled(False)
        self.ui.searchButton.setText("Search")
        self.new_text.emit()

    def activateInfoLabels(self):
        for widget in self.info_widgets:
            widget.setEnabled(self.ui.showInfoBox.isChecked())

    def updateInfo(self, to_find: str, total_lines: int, matches: int):
        info_labels_is_active = self.ui.info1Label.isEnabled()
        if info_labels_is_active:
            self.ui.info1Label.setText(f'Line to find: "{to_find}"')
            self.ui.info2Label.setText(f"Total lines: {total_lines}")
            self.ui.info3Label.setText(f"Matches total: {matches}")

    def search(self):
        to_find = self.ui.lineEdit.text().strip().lower()
        if not to_find:
            QtWidgets.QMessageBox.warning(self, "Warning", "You haven't written any letters")
            return
        self.to_find = to_find
        matches, total_lines, temp = 0, 0, 0
        letters_iterated = 0
        for line in self.strings:
            line = line.strip().lower()
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
            self.ui.lineEdit.setText("Found!")
            self.ui.previousButton.setEnabled(False)
            self.ui.nextButton.setEnabled(True)
            self.ui.saveMatchesButton.setEnabled(True)
            self.ui.replaceModeButton.setEnabled(True)
            self.ui.showInfoBox.setEnabled(False)
        else:
            self.ui.lineEdit.setText("Not found!")
        self.ui.lineEdit.setReadOnly(True)

    def replaceButton(self):
        self.replace_with = self.ui.lineEdit.text().strip().lower()
        if not self.replace_with:
            QtWidgets.QMessageBox.warning(self, "Warning", "You haven't written any letters!")
            return
        self.replace.emit()
        self.ui.lineEdit.setReadOnly(True)
        self.ui.resetReplaceButton.setEnabled(True)

    def handleControlButton(self):
        button_text = self.ui.searchButton.text()
        if button_text == "Search":
            self.searchButton()
        elif button_text == "Replace":
            self.replaceButton()
        self.ui.searchButton.setEnabled(False)

    def saveMatches(self):
        if not self.buffer:
            QtWidgets.QMessageBox.warning(self, "Warning", "You have to search something to save")
            return
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file")
        if not file:
            return
        try:
            with open(file, "w", encoding="utf-8") as f:
                for line in self.line_buffer:
                    f.write(line + "\n")
                QtWidgets.QMessageBox.information(self, "Writing", "Matches were saved!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Fail", "You don't have permissions to write in file!")
            return

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.textEdit.clear()

        # styles
        self.setStyleSheet(parse_qss("QPushButton") + "\n\n" + parse_qss("QDialog") + "\n\n" + parse_qss("QLabel"))
        self.ui.centralwidget.setStyleSheet("background-color: #4c4c4c;")
        self.ui.menubar.setStyleSheet(parse_qss("QMenuBar") + "\n\n" + parse_qss("QMenu"))
        self.ui.textEdit.setStyleSheet(parse_qss("QScrollBar") + "\n\n" + parse_qss("QTextEdit"))
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
        self.context_menu = QtWidgets.QMenu(self)  # right click

        # menuFile
        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSave_as.triggered.connect(self.saveAsFile)
        self.ui.actionExit.triggered.connect(self.exit)

        # menuEdit
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        for _clr in self.colors:
            temp_widget = getattr(self.ui, "action" + _clr)
            temp_widget.triggered.connect(lambda _, clr=_clr: self.color(clr.lower()))
        self.ui.actionResetColor.triggered.connect(lambda: self.ui.textEdit.setTextColor(QtGui.QColor("white")))
        self.ui.actionReadOnly.triggered.connect(lambda: self.ui.textEdit.setReadOnly(not self.ui.textEdit.isReadOnly()))
        for widget, format in self.format_table.items():
            widget.triggered.connect(lambda _, fmt=format: self.formatingString(fmt))

        for action, weight in self.weight_table.items():
            action.triggered.connect(lambda _, w=weight: self.changeWeight(w))
        self.ui.actionResetStyle.triggered.connect(self.resetStyles)

        # contextMenu
        self.ui.actionDelete = QtGui.QAction("Delete", self)
        self.ui.actionDelete.setObjectName("actionDelete")
        self.ui.actionCopy = QtGui.QAction("Copy", self)
        self.ui.actionCopy.setObjectName("actionCopy")
        self.ui.actionPaste = QtGui.QAction("Paste", self)
        self.ui.actionPaste.setObjectName("actionPaste")
        self.ui.actionCut = QtGui.QAction("Cut", self)
        self.ui.actionPaste.setObjectName("actionCut")
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
        self.context_menu.setStyleSheet(parse_qss("QMenu"))

        # Feautures
        self.ui.actionFind.triggered.connect(self.createFindWindow)

    def exit(self) -> int:
        code = self.saveChanges()
        return code

    def showContextMenuEvent(self, pos):
        self.context_menu.exec(self.ui.textEdit.viewport().mapToGlobal(pos))

    def closeEvent(self, a0):
        code = self.exit()
        if code != 0:
            return super().closeEvent(a0)
        a0.ignore()

    def _fileSaver(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file")
        if file:
            self.file = file

    def _writeLines(self):
        if self.file:
            try:
                with open(self.file, "w", encoding="utf-8") as f:
                    f.writelines(self.ui.textEdit.toPlainText()) 
            except PermissionError:
                QtWidgets.QMessageBox.warning(self, "Permissions", "You don't have rights to apply changes")

    def saveChanges(self) -> int:  # -1 - leave without save, 0 - not leave, 1 - leave with save
        if self.ui.textEdit.toPlainText():
            choice = QtWidgets.QMessageBox.question(self, "Warning", "Do you want to save the changes?", QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel, QtWidgets.QMessageBox.StandardButton.Save)
            if choice == QtWidgets.QMessageBox.StandardButton.Save:
                if not self.file:
                    self._fileSaver()
                self._writeLines()
                return 1
            elif choice == QtWidgets.QMessageBox.StandardButton.Cancel:
                return 0
            elif choice == QtWidgets.QMessageBox.StandardButton.No:
                return -1

    def newFile(self):
        code = self.saveChanges()
        if code != 0:
            self.ui.textEdit.clear()

    def openFile(self):
        self.saveChanges()
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", filter="*.txt")
        if file:
            self.file = file
            self.ui.textEdit.clear()
            try:
                with open(self.file, "r", encoding="utf-8") as f:
                    for line in f:
                        self.ui.textEdit.append(line[:-1])
            except UnicodeError:
                QtWidgets.QMessageBox.warning(self, "Permissions", "File contains non utf-8 symbols and can't be viewed!")

    def saveFile(self):
        if not self.file:
            self._fileSaver()
        self._writeLines()

    def saveAsFile(self):
        self._fileSaver()
        self._writeLines()

    def color(self, clr):
        text_cursor = self.ui.textEdit.textCursor()
        temp_clr = QtGui.QColor(clr)
        if not self.ui.textEdit.toPlainText():
            return
        self.ui.textEdit.setTextColor(temp_clr)
        text_cursor.clearSelection()

    def changeWeight(self, value: int):
        self.ui.textEdit.setFontWeight(value)

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

    def replaceText(self, to_replace: str, replace_with: str, mode: int) -> None:
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

    def getLines(self):
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

    def createFindWindow(self):
        text = self.getLines()
        if text:
            window = FindWindow(text)
            window.setStyleSheet(parse_qss("QDialog") + "\n\n" + parse_qss("QLabel") + "\n\n" + parse_qss("QPushButton"))
            window.ui.lineEdit.setStyleSheet(parse_qss("QLineEdit"))
            window.ui.showInfoBox.setStyleSheet(parse_qss("QCheckBox"))
            window.ui.verticalLayoutWidget.setStyleSheet("QLabel {font-size: 11pt;}")
            window.ui.previousButton.clicked.connect(lambda: self.viewText(window, 0))
            window.ui.nextButton.clicked.connect(lambda: self.viewText(window, 1))
            window.ui.resetReplaceButton.clicked.connect(lambda: self.replaceText(window.to_find, window.replace_with, 0))
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
