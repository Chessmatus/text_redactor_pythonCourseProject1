from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QDialog, QMessageBox
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(750, 300, 500, 500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.cursor = self.text_edit.textCursor()
        self.text_edit.setTextCursor(self.cursor)

        self.action_open = QtWidgets.QAction()
        self.action_save = QtWidgets.QAction()
        self.action_save_as = QtWidgets.QAction()
        self.action_new = QtWidgets.QAction()
        self.action_find = QtWidgets.QAction()
        self.action_find_replace = QtWidgets.QAction()
        self.action_quit = QtWidgets.QAction()
        self.action_cut = QtWidgets.QAction()
        self.action_copy = QtWidgets.QAction()
        self.action_paste = QtWidgets.QAction()
        self.action_delete = QtWidgets.QAction()

        self.text_red = QtWidgets.QAction()
        self.text_black = QtWidgets.QAction()
        self.text_white = QtWidgets.QAction()
        self.text_yellow = QtWidgets.QAction()
        self.text_blue = QtWidgets.QAction()
        self.text_green = QtWidgets.QAction()
        self.text_grey = QtWidgets.QAction()

        self.back_red = QtWidgets.QAction()
        self.back_black = QtWidgets.QAction()
        self.back_white = QtWidgets.QAction()
        self.back_yellow = QtWidgets.QAction()
        self.back_blue = QtWidgets.QAction()
        self.back_green = QtWidgets.QAction()
        self.back_grey = QtWidgets.QAction()
        self.light_mode = QtWidgets.QAction()
        self.dark_mode = QtWidgets.QAction()

        self.menu_bar = QMenuBar(self)
        self.create_menu_bar()

        self.f_name = ''

        self.search_dialog = QDialog()
        self.search_replace_dialog = QDialog()

    def create_menu_bar(self):
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        edit_menu = QMenu("&Правка", self)
        self.menu_bar.addMenu(edit_menu)

        view_menu = QMenu("&Вид", self)
        self.menu_bar.addMenu(view_menu)
        text_color = QMenu("&Цвет текста", self)
        view_menu.addMenu(text_color)
        back_color = QMenu("&Фон текста", self)
        view_menu.addMenu(back_color)
        back = QMenu("&Фон", self)
        view_menu.addMenu(back)

        file_menu.addAction(self.action_new)
        self.action_new.setText("Новый")
        self.action_new.setShortcut(QKeySequence.New)
        self.action_new.triggered.connect(self.new_file)

        file_menu.addAction(self.action_open)
        self.action_open.setText("Открыть")
        self.action_open.setShortcut(QKeySequence.Open)
        self.action_open.triggered.connect(self.open_file)

        file_menu.addSeparator()

        file_menu.addAction(self.action_save)
        self.action_save.setText("Сохранить")
        self.action_save.setShortcut(QKeySequence.Save)
        self.action_save.triggered.connect(self.save_file)

        file_menu.addAction(self.action_save_as)
        self.action_save_as.setText("Сохранить как...")
        self.action_save_as.setShortcut(QKeySequence.SaveAs)
        self.action_save_as.triggered.connect(self.save_file_as)

        file_menu.addSeparator()

        file_menu.addAction(self.action_quit)
        self.action_quit.setText("Выйти")
        self.action_quit.setShortcut(QKeySequence.Quit)
        self.action_quit.triggered.connect(self.quit)

        edit_menu.addAction(self.action_cut)
        self.action_cut.setText("Вырезать")
        self.action_cut.setShortcut(QKeySequence.Cut)
        self.action_cut.triggered.connect(self.cut)

        edit_menu.addAction(self.action_copy)
        self.action_copy.setText("Копировать")
        self.action_copy.setShortcut(QKeySequence.Copy)
        self.action_copy.triggered.connect(self.copy)

        edit_menu.addAction(self.action_paste)
        self.action_paste.setText("Вставить")
        self.action_paste.setShortcut(QKeySequence.Paste)
        self.action_paste.triggered.connect(self.paste)

        edit_menu.addSeparator()

        edit_menu.addAction(self.action_delete)
        self.action_delete.setText("Удалить")
        self.action_delete.setShortcut(QKeySequence.Delete)
        self.action_delete.triggered.connect(self.delete)

        edit_menu.addSeparator()

        edit_menu.addAction(self.action_find)
        self.action_find.setText("Найти")
        self.action_find.setShortcut(QKeySequence.Find)
        self.action_find.triggered.connect(self.find_)

        edit_menu.addAction(self.action_find_replace)
        self.action_find_replace.setText("Найти и заменить")
        self.action_find_replace.setShortcut(QKeySequence.Replace)
        self.action_find_replace.triggered.connect(self.find_replace)

        text_color.addAction(self.text_black)
        self.text_black.setText("Черный")
        self.text_black.triggered.connect(self.t_black)

        text_color.addAction(self.text_red)
        self.text_red.setText("Красный")
        self.text_red.triggered.connect(self.t_red)

        text_color.addAction(self.text_blue)
        self.text_blue.setText("Синий")
        self.text_blue.triggered.connect(self.t_blue)

        text_color.addAction(self.text_green)
        self.text_green.setText("Зеленый")
        self.text_green.triggered.connect(self.t_green)

        text_color.addAction(self.text_yellow)
        self.text_yellow.setText("Желтый")
        self.text_yellow.triggered.connect(self.t_yellow)

        text_color.addAction(self.text_white)
        self.text_white.setText("Белый")
        self.text_white.triggered.connect(self.t_white)

        text_color.addAction(self.text_grey)
        self.text_grey.setText("Серый")
        self.text_grey.triggered.connect(self.t_grey)

        back_color.addAction(self.back_black)
        self.back_black.setText("Черный")
        self.back_black.triggered.connect(self.b_black)

        back_color.addAction(self.back_red)
        self.back_red.setText("Красный")
        self.back_red.triggered.connect(self.b_red)

        back_color.addAction(self.back_blue)
        self.back_blue.setText("Синий")
        self.back_blue.triggered.connect(self.b_blue)

        back_color.addAction(self.back_green)
        self.back_green.setText("Зеленый")
        self.back_green.triggered.connect(self.b_green)

        back_color.addAction(self.back_yellow)
        self.back_yellow.setText("Желтый")
        self.back_yellow.triggered.connect(self.b_yellow)

        back_color.addAction(self.back_white)
        self.back_white.setText("Белый")
        self.back_white.triggered.connect(self.b_white)

        back_color.addAction(self.back_grey)
        self.back_grey.setText("Серый")
        self.back_grey.triggered.connect(self.b_grey)

        back.addAction(self.light_mode)
        self.light_mode.setText("Светлый")
        self.light_mode.triggered.connect(self.light_m)

        back.addAction(self.dark_mode)
        self.dark_mode.setText("Темный")
        self.dark_mode.triggered.connect(self.dark_m)

    def open_file(self):
        self.f_name = QFileDialog.getOpenFileName(self, "Открыть файл", filter='Text files (*.txt)',
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'r') as f:
                self.text_edit.setTextColor(QColor("black"))
                self.text_edit.setTextBackgroundColor(QColor("white"))
                data = f.read()
                self.text_edit.setText(data)
        except FileNotFoundError:
            print("No such file")
        except PermissionError:
            self.f_name = ''
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не удалось сохранить файл. "
                          "Недостаточно прав для сохранения файла. "
                          "Убедитесь в правильности указанного адреса и попробуйте еще раз.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()

    def save_file(self):
        if self.f_name == '':
            self.f_name = QFileDialog.getSaveFileName(self, "Сохранить файл", filter='Text files (*.txt)',
                                                      options=QFileDialog.DontUseNativeDialog)[0]
            try:
                with open(self.f_name, 'w') as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("No such file")
            except PermissionError:
                self.f_name = ''
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Не удалось сохранить файл. "
                              "Недостаточно прав для сохранения файла. "
                              "Убедитесь в правильности указанного адреса и попробуйте еще раз.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)

                error.exec_()
        else:
            with open(self.f_name, 'w') as f:
                text = self.text_edit.toPlainText()
                f.write(text)

    def save_file_as(self):
        self.f_name = QFileDialog.getSaveFileName(self, "Сохранить файл", filter='Text files (*.txt)',
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'w') as f:
                text = self.text_edit.toPlainText()
                f.write(text)
        except FileNotFoundError:
            print("No such file")
        except PermissionError:
            self.f_name = ''
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не удалось сохранить файл. "
                          "Недостаточно прав для сохранения файла. "
                          "Убедитесь в правильности указанного адреса и попробуйте еще раз.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()

    def new_file(self):
        self.f_name = ''
        self.text_edit.clear()
        self.text_edit.setTextColor(QColor("black"))
        self.text_edit.setTextBackgroundColor(QColor("white"))

    def cut(self):
        self.text_edit.cut()

    def copy(self):
        self.text_edit.copy()

    def paste(self):
        self.text_edit.paste()

    def delete(self):
        self.text_edit.textCursor().removeSelectedText()

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
        if not self.text_edit.find(words):
            self.cursor.setPosition(0)
            self.text_edit.setTextCursor(self.cursor)
            self.text_edit.find(words)

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
        if not self.text_edit.find(words):
            self.cursor.setPosition(0)
            self.text_edit.setTextCursor(self.cursor)
            if not self.text_edit.find(words):
                self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        self.text_edit.textCursor().removeSelectedText()
        self.text_edit.textCursor().insertText(replace_with)
        self.search_replace_dialog.replace_btn.setEnabled(False)

    def replace_all_btn_clicked(self):
        replace_with = self.search_replace_dialog.line_edit_2.text()
        replace_what = self.search_replace_dialog.line_edit_1.text()
        text = self.text_edit.toPlainText()
        text = text.replace(replace_what, replace_with)
        self.text_edit.setText(text)

    def t_black(self):
        self.text_edit.setTextColor(QColor("black"))

    def t_red(self):
        self.text_edit.setTextColor(QColor("red"))

    def t_blue(self):
        self.text_edit.setTextColor(QColor("blue"))

    def t_white(self):
        self.text_edit.setTextColor(QColor("white"))

    def t_green(self):
        self.text_edit.setTextColor(QColor("green"))

    def t_yellow(self):
        self.text_edit.setTextColor(QColor("yellow"))

    def t_grey(self):
        self.text_edit.setTextColor(QColor("grey"))

    def b_black(self):
        self.text_edit.setTextBackgroundColor(QColor("black"))

    def b_red(self):
        self.text_edit.setTextBackgroundColor(QColor("red"))

    def b_blue(self):
        self.text_edit.setTextBackgroundColor(QColor("blue"))

    def b_white(self):
        self.text_edit.setTextBackgroundColor(QColor("white"))

    def b_green(self):
        self.text_edit.setTextBackgroundColor(QColor("green"))

    def b_yellow(self):
        self.text_edit.setTextBackgroundColor(QColor("yellow"))

    def b_grey(self):
        self.text_edit.setTextBackgroundColor(QColor("grey"))

    def light_m(self):
        self.setStyleSheet('''QTextEdit{background-color: #FFFFFF; color: #000000}''')

    def dark_m(self):
        self.setStyleSheet('''QTextEdit{background-color: #000000; color: #FFFFFF}''')

    def quit(self):
        self.close()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
