from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu, QFileDialog, QMessageBox
from PyQt5.QtGui import QKeySequence, QColor


class FileMenu(QMenu):
    def __init__(self, menu_bar):
        self.window = menu_bar.window
        self.menu_bar = menu_bar

        super().__init__("&Файл")

        self.f_name = ''

        self.action_open = QtWidgets.QAction()
        self.action_save = QtWidgets.QAction()
        self.action_save_as = QtWidgets.QAction()
        self.action_new = QtWidgets.QAction()
        self.action_quit = QtWidgets.QAction()

        self.add_action(self.action_new, "Новый", QKeySequence.New, self.new_file)
        self.add_action(self.action_open, "Открыть", QKeySequence.Open, self.open_file)
        self.addSeparator()
        self.add_action(self.action_save, "Сохранить", QKeySequence.Save, self.save_file)
        self.add_action(self.action_save_as, "Сохранить как...", QKeySequence.SaveAs, self.save_file_as)
        self.addSeparator()
        self.add_action(self.action_quit, "Выйти", QKeySequence.Quit, self.quit)

    def add_action(self, action, name, shortcut, connect):
        action.setText(name)
        action.setShortcut(shortcut)
        action.triggered.connect(connect)
        self.addAction(action)

    def open_file(self):
        self.f_name = QFileDialog.getOpenFileName(self.window, "Открыть файл", filter='Text files (*.txt)',
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'r') as f:
                self.window.text_edit.setTextColor(QColor("black"))
                self.window.text_edit.setTextBackgroundColor(QColor("white"))
                data = f.read()
                self.window.text_edit.setText(data)
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
            self.f_name = QFileDialog.getSaveFileName(self.window, "Сохранить файл", filter='Text files (*.txt)',
                                                      options=QFileDialog.DontUseNativeDialog)[0]
            try:
                with open(self.f_name, 'w') as f:
                    text = self.window.text_edit.toPlainText()
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
                text = self.window.text_edit.toPlainText()
                f.write(text)

    def save_file_as(self):
        self.f_name = QFileDialog.getSaveFileName(self.window, "Сохранить файл", filter='Text files (*.txt)',
                                                  options=QFileDialog.DontUseNativeDialog)[0]
        try:
            with open(self.f_name, 'w') as f:
                text = self.window.text_edit.toPlainText()
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
        self.window.text_edit.clear()
        self.window.text_edit.setTextColor(QColor("black"))
        self.window.text_edit.setTextBackgroundColor(QColor("white"))

    def quit(self):
        self.window.close()

