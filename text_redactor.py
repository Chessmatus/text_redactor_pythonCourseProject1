from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QDialog, QShortcut
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(750, 300, 500, 500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.cursor = self.text_edit.textCursor()

        self.action_open = QtWidgets.QAction()
        self.action_save = QtWidgets.QAction()
        self.action_save_as = QtWidgets.QAction()
        self.action_new = QtWidgets.QAction()
        self.action_find = QtWidgets.QAction()
        self.action_find_replace = QtWidgets.QAction()

        self.menu_bar = QMenuBar(self)
        self.create_menu_bar()

        self.f_name = ''

        self.search_dialog = QDialog()
        self.search_replace_dialog = QDialog()

        self.search_pos = -1
        self.search_first = True

    def create_menu_bar(self):
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        find_menu = QMenu("&Найти", self)
        self.menu_bar.addMenu(find_menu)

        file_menu.addAction(self.action_new)
        self.action_new.setText("Новый")
        self.action_new.setShortcut(QKeySequence.New)
        self.action_new.triggered.connect(self.new_file)

        file_menu.addAction(self.action_open)
        self.action_open.setText("Открыть")
        self.action_open.setShortcut(QKeySequence.Open)
        self.action_open.triggered.connect(self.open_file)

        file_menu.addAction(self.action_save)
        self.action_save.setText("Сохранить")
        self.action_save.setShortcut(QKeySequence.Save)
        self.action_save.triggered.connect(self.save_file)

        file_menu.addAction(self.action_save_as)
        self.action_save_as.setText("Сохранить как...")
        self.action_save_as.setShortcut(QKeySequence.SaveAs)
        self.action_save_as.triggered.connect(self.save_file_as)

        find_menu.addAction(self.action_find)
        self.action_find.setText("Найти")
        self.action_find.setShortcut(QKeySequence.Find)
        self.action_find.triggered.connect(self.find)

        find_menu.addAction(self.action_find_replace)
        self.action_find_replace.setText("Найти и заменить")
        self.action_find_replace.setShortcut(QKeySequence.Replace)
        self.action_find_replace.triggered.connect(self.find_replace)

    def open_file(self):
        self.f_name = QFileDialog.getOpenFileName(self, "Открыть файл", "/home",
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'r') as f:
                data = f.read()
                self.text_edit.setText(data)
        except FileNotFoundError:
            print("No such file")

    def save_file(self):
        if self.f_name == '':
            self.f_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "/home",
                                                      options=QFileDialog.DontUseNativeDialog)[0]
            try:
                with open(self.f_name, 'w') as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("No such file")
        else:
            with open(self.f_name, 'w') as f:
                text = self.text_edit.toPlainText()
                f.write(text)

    def save_file_as(self):
        self.f_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "/home",
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'w') as f:
                text = self.text_edit.toPlainText()
                f.write(text)
        except FileNotFoundError:
            print("No such file")

    def new_file(self):
        self.f_name = ''
        self.text_edit.clear()

    def find(self):
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
        if not self.text_edit.find(words):
            self.cursor.setPosition(0)
            self.text_edit.setTextCursor(self.cursor)
            self.text_edit.find(words)

    def enable_btn(self, text):
        self.search_pos = 0
        self.search_first = True
        self.cursor.setPosition(0)
        self.text_edit.setTextCursor(self.cursor)
        if not text:
            self.search_replace_dialog.search_btn.setEnabled(False)
            self.search_replace_dialog.replace_btn.setEnabled(False)
            self.search_replace_dialog.replace_all_btn.setEnabled(False)
        else:
            self.search_replace_dialog.search_btn.setEnabled(True)
            self.search_replace_dialog.replace_all_btn.setEnabled(True)

    def get_word_pos(self, words):
        text = self.text_edit.toPlainText()
        if self.search_first:
            self.search_pos = text.find(words)
            self.search_first = False
        else:
            pos = text[self.search_pos + len(words):].find(words)
            if pos == -1:
                self.search_pos = -1
            else:
                self.search_pos = pos + self.search_pos + len(words)
        return self.search_pos

    def search_btn_clicked(self):
        self.search_replace_dialog.replace_btn.setEnabled(True)
        text = self.text_edit.toPlainText()
        words = self.search_replace_dialog.line_edit_1.text()

        if self.search_pos + len(words) >= len(text) or not self.get_word_pos(words) + 1:
            self.search_pos = 0
            self.search_first = True
            self.get_word_pos(words)

        if not self.text_edit.find(words):
            self.cursor.setPosition(0)
            self.text_edit.setTextCursor(self.cursor)
            if not self.text_edit.find(words):
                self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        replace_what = self.search_replace_dialog.line_edit_1.text()
        text = self.text_edit.toPlainText()
        text = text[:self.search_pos] + replace_with + text[self.search_pos + len(replace_what):]
        self.text_edit.setText(text)
        self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_all_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        replace_what = self.search_replace_dialog.line_edit_1.text()
        text = self.text_edit.toPlainText()
        text = text.replace(replace_what, replace_with)
        self.text_edit.setText(text)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
