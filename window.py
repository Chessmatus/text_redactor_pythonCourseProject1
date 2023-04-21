import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from menu_bar import MenuBar


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(750, 300, 500, 500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.cursor = self.text_edit.textCursor()
        self.text_edit.setTextCursor(self.cursor)

        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
