from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
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

    def create_menu_bar(self):
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        file_menu.addAction('Открыть', self.action_clicked)
        file_menu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            f_name = QFileDialog().getOpenFileName(self)[0]

            try:
                f = open(f_name, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Сохранить":
            f_name = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(f_name, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")

        """open_file = fileMenu.addMenu("&Открыть")
        save_file = fileMenu.addMenu("&Сохранить")"""


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()