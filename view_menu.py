from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QColor


class TextColor(QMenu):
    def __init__(self, menu_bar):
        super().__init__("&Цвет текста")

        self.menu_bar = menu_bar
        self.window = menu_bar.window

        self.text_red = QtWidgets.QAction()
        self.text_black = QtWidgets.QAction()
        self.text_white = QtWidgets.QAction()
        self.text_yellow = QtWidgets.QAction()
        self.text_blue = QtWidgets.QAction()
        self.text_green = QtWidgets.QAction()
        self.text_grey = QtWidgets.QAction()

        self.add_color(self.text_black, "Черный", self.t_black)
        self.add_color(self.text_red, "Красный", self.t_red)
        self.add_color(self.text_blue, "Синий", self.t_blue)
        self.add_color(self.text_green, "Зеленый", self.t_green)
        self.add_color(self.text_yellow, "Желтый", self.t_yellow)
        self.add_color(self.text_white, "Белый", self.t_white)
        self.add_color(self.text_grey, "Серый", self.t_grey)

    def add_color(self, action, color_name, connect):
        action.setText(color_name)
        action.triggered.connect(connect)
        self.addAction(action)

    def t_black(self):
        self.window.text_edit.setTextColor(QColor("black"))

    def t_red(self):
        self.window.text_edit.setTextColor(QColor("red"))

    def t_blue(self):
        self.window.text_edit.setTextColor(QColor("blue"))

    def t_white(self):
        self.window.text_edit.setTextColor(QColor("white"))

    def t_green(self):
        self.window.text_edit.setTextColor(QColor("green"))

    def t_yellow(self):
        self.window.text_edit.setTextColor(QColor("yellow"))

    def t_grey(self):
        self.window.text_edit.setTextColor(QColor("grey"))


class TextBackColor(QMenu):
    def __init__(self, menu_bar):
        super().__init__("&Фон текста")

        self.menu_bar = menu_bar
        self.window = menu_bar.window

        self.back_red = QtWidgets.QAction()
        self.back_black = QtWidgets.QAction()
        self.back_white = QtWidgets.QAction()
        self.back_yellow = QtWidgets.QAction()
        self.back_blue = QtWidgets.QAction()
        self.back_green = QtWidgets.QAction()
        self.back_grey = QtWidgets.QAction()

        self.add_color(self.back_black, "Черный", self.b_black)
        self.add_color(self.back_red, "Красный", self.b_red)
        self.add_color(self.back_blue, "Синий", self.b_blue)
        self.add_color(self.back_green, "Зеленый", self.b_green)
        self.add_color(self.back_yellow, "Желтый", self.b_yellow)
        self.add_color(self.back_white, "Белый", self.b_white)
        self.add_color(self.back_grey, "Серый", self.b_grey)

    def add_color(self, action, color_name, connect):
        action.setText(color_name)
        action.triggered.connect(connect)
        self.addAction(action)

    def b_black(self):
        self.window.text_edit.setTextBackgroundColor(QColor("black"))

    def b_red(self):
        self.window.text_edit.setTextBackgroundColor(QColor("red"))

    def b_blue(self):
        self.window.text_edit.setTextBackgroundColor(QColor("blue"))

    def b_white(self):
        self.window.text_edit.setTextBackgroundColor(QColor("white"))

    def b_green(self):
        self.window.text_edit.setTextBackgroundColor(QColor("green"))

    def b_yellow(self):
        self.window.text_edit.setTextBackgroundColor(QColor("yellow"))

    def b_grey(self):
        self.window.text_edit.setTextBackgroundColor(QColor("grey"))


class Background(QMenu):
    def __init__(self, menu_bar):
        super().__init__("&Тема")

        self.menu_bar = menu_bar
        self.window = menu_bar.window

        self.light_mode = QtWidgets.QAction()
        self.dark_mode = QtWidgets.QAction()

        self.add_color(self.light_mode, "Светлый", self.light_m)
        self.add_color(self.dark_mode, "Темный", self.dark_m)

    def add_color(self, action, color_name, connect):
        action.setText(color_name)
        action.triggered.connect(connect)
        self.addAction(action)

    def light_m(self):
        self.window.setStyleSheet('''QTextEdit{background-color: #FFFFFF; color: #000000}''')

    def dark_m(self):
        self.window.setStyleSheet('''QTextEdit{background-color: #000000; color: #FFFFFF}''')


class ViewMenu(QMenu):
    def __init__(self, menu_bar):
        super().__init__("&Вид")

        self.menu_bar = menu_bar
        self.window = menu_bar.window

        self.text_color_menu = TextColor(menu_bar)
        self.t_back_color_menu = TextBackColor(menu_bar)
        self.background = Background(menu_bar)

        self.addMenu(self.text_color_menu)
        self.addMenu(self.t_back_color_menu)
        self.addMenu(self.background)
