from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu, QDialog
from PyQt5.QtGui import QKeySequence


class EditMenu(QMenu):
    def __init__(self, menu_bar):
        super().__init__("&Правка")

        self.window = menu_bar.window
        self.menu_bar = menu_bar

        self.action_find = QtWidgets.QAction()
        self.action_find_replace = QtWidgets.QAction()
        self.action_cut = QtWidgets.QAction()
        self.action_copy = QtWidgets.QAction()
        self.action_paste = QtWidgets.QAction()
        self.action_delete = QtWidgets.QAction()

        self.add_action(self.action_cut, "Вырезать", QKeySequence.Cut, self.cut)
        self.add_action(self.action_copy, "Копировать", QKeySequence.Copy, self.copy)
        self.add_action(self.action_paste, "Вставить", QKeySequence.Paste, self.paste)
        self.addSeparator()
        self.add_action(self.action_delete, "Удалить", QKeySequence.Delete, self.delete)
        self.addSeparator()
        self.add_action(self.action_find, "Найти", QKeySequence.Find, self.find_)
        self.add_action(self.action_find_replace, "Найти и заменить", QKeySequence.Replace,
                        self.find_replace)

        self.search_dialog = QDialog()
        self.search_replace_dialog = QDialog()

    def add_action(self, action, name, shortcut, connect):
        action.setText(name)
        action.setShortcut(shortcut)
        action.triggered.connect(connect)
        self.addAction(action)

    def cut(self):
        self.window.text_edit.cut()

    def copy(self):
        self.window.text_edit.copy()

    def paste(self):
        self.window.text_edit.paste()

    def delete(self):
        self.window.text_edit.textCursor().removeSelectedText()

    def find_(self):
        self.search_dialog.setWindowTitle("Найти")
        self.search_dialog.resize(260, 35)
        self.search_dialog.line_edit = QtWidgets.QLineEdit(self.search_dialog)
        self.search_dialog.line_edit.setGeometry(60, 0, 200, 35)
        self.search_dialog.find_btn = QtWidgets.QPushButton("Найти", self.search_dialog)
        self.search_dialog.find_btn.setGeometry(0, 0, 60, 35)
        self.search_dialog.find_btn.clicked.connect(self.find_btn_clicked)

        self.search_dialog.exec_()

    def find_replace(self):
        self.search_replace_dialog.setWindowTitle("Найти и заменить")
        self.search_replace_dialog.resize(450, 175)

        self.search_replace_dialog.search_label = QtWidgets.QLabel("Найти", self.search_replace_dialog)
        self.search_replace_dialog.search_label.move(55, 25)
        self.search_replace_dialog.search_label.resize(35, 35)
        self.search_replace_dialog.search_label.adjustSize()

        self.search_replace_dialog.line_edit_1 = QtWidgets.QLineEdit(self.search_replace_dialog)
        self.search_replace_dialog.line_edit_1.setGeometry(115, 15, 300, 35)
        self.search_replace_dialog.line_edit_1.textChanged.connect(self.enable_btn)

        self.search_replace_dialog.replace_label = QtWidgets.QLabel("Заменить на", self.search_replace_dialog)
        self.search_replace_dialog.replace_label.move(10, 80)
        self.search_replace_dialog.replace_label.resize(35, 35)
        self.search_replace_dialog.replace_label.adjustSize()

        self.search_replace_dialog.line_edit_2 = QtWidgets.QLineEdit(self.search_replace_dialog)
        self.search_replace_dialog.line_edit_2.setGeometry(115, 70, 300, 35)

        self.search_replace_dialog.search_btn = QtWidgets.QPushButton("Найти", self.search_replace_dialog)
        self.search_replace_dialog.search_btn.setGeometry(365, 125, 50, 35)
        self.search_replace_dialog.search_btn.setEnabled(False)
        self.search_replace_dialog.search_btn.clicked.connect(self.search_btn_clicked)

        self.search_replace_dialog.replace_btn = QtWidgets.QPushButton("Заменить", self.search_replace_dialog)
        self.search_replace_dialog.replace_btn.setGeometry(280, 125, 75, 35)
        self.search_replace_dialog.replace_btn.setEnabled(False)
        self.search_replace_dialog.replace_btn.clicked.connect(self.replace_btn_clicked)

        self.search_replace_dialog.replace_all_btn = QtWidgets.QPushButton("Заменить все",
                                                                           self.search_replace_dialog)
        self.search_replace_dialog.replace_all_btn.setGeometry(165, 125, 105, 35)
        self.search_replace_dialog.replace_all_btn.setEnabled(False)
        self.search_replace_dialog.replace_all_btn.clicked.connect(self.replace_all_btn_clicked)

        self.search_replace_dialog.exec_()

    def find_btn_clicked(self):
        words = self.search_dialog.line_edit.text()
        if not self.window.text_edit.find(words):
            self.window.cursor.setPosition(0)
            self.window.text_edit.setTextCursor(self.window.cursor)
            self.window.text_edit.find(words)

    def enable_btn(self, text):
        if not text:
            self.search_replace_dialog.search_btn.setEnabled(False)
            self.search_replace_dialog.replace_btn.setEnabled(False)
            self.search_replace_dialog.replace_all_btn.setEnabled(False)
        else:
            self.search_replace_dialog.search_btn.setEnabled(True)
            self.search_replace_dialog.replace_all_btn.setEnabled(True)

    def search_btn_clicked(self):
        self.search_replace_dialog.replace_btn.setEnabled(True)
        words = self.search_replace_dialog.line_edit_1.text()
        if not self.window.text_edit.find(words):
            self.window.cursor.setPosition(0)
            self.window.text_edit.setTextCursor(self.window.cursor)
            if not self.window.text_edit.find(words):
                self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        self.window.text_edit.textCursor().removeSelectedText()
        self.window.text_edit.textCursor().insertText(replace_with)
        self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_all_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        replace_what = self.search_replace_dialog.line_edit_1.text()
        text = self.window.text_edit.toPlainText()
        text = text.replace(replace_what, replace_with)
        self.window.text_edit.setText(text)

