from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QDialog
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(750, 300, 500, 500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.menu_bar = QMenuBar(self)
        self.create_menu_bar()

        self.search_dialog = QDialog()

    def create_menu_bar(self):
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        file_menu.addAction("Открыть", self.action_clicked)
        file_menu.addAction("Сохранить", self.action_clicked)
        file_menu.addAction("Найти", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            f_name = QFileDialog.getOpenFileName(self, "Открыть файл", "/home",
                                                 options=QFileDialog.DontUseNativeDialog)[0]
            try:
                with open(f_name, 'r') as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Сохранить":
            f_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "/home",
                                                 options=QFileDialog.DontUseNativeDialog)[0]
            try:
                with open(f_name, 'w') as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Найти":
            self.search_dialog.setWindowTitle("Найти")
            self.search_dialog.resize(260, 35)
            self.search_dialog.line_edit = QtWidgets.QLineEdit(self.search_dialog)
            self.search_dialog.line_edit.setGeometry(61, 0, 200, 35)
            self.search_dialog.find_btn = QtWidgets.QPushButton("Найти:", self.search_dialog)
            self.search_dialog.find_btn.setGeometry(0, 0, 60, 35)
            self.search_dialog.find_btn.clicked.connect(self.find_btn_clicked)

            self.search_dialog.exec_()

    def find_btn_clicked(self):
        words = self.search_dialog.line_edit.text()
        if not self.text_edit.find(words):
            cursor = self.text_edit.textCursor()
            cursor.setPosition(0)
            self.text_edit.setTextCursor(cursor)
            self.text_edit.find(words)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
