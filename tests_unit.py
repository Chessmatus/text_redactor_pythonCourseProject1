import sys
import unittest
import PyQt5
from PyQt5.QtWidgets import QApplication
from window import Window


class WindowTest(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = Window()

    def test_window_name(self):
        self.assertEqual(self.window.windowTitle(), "Текстовый редактор")

    def test_window_geometry(self):
        self.assertEqual(self.window.geometry(), PyQt5.QtCore.QRect(750, 300, 500, 500))

    def tearDown(self):
        self.app.quit()


class FileMenuTest(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = Window()

    def test_open_file(self):
        self.window.menu_bar.file_menu.open_file()
        if self.window.menu_bar.file_menu.f_name != '':
            with open(self.window.menu_bar.file_menu.f_name, 'r') as f:
                self.assertEqual(f.read(), self.window.text_edit.toPlainText())
        else:
            self.assertEqual(self.window.text_edit.toPlainText(), '')

    def test_save_file(self):
        self.window.text_edit.setText("hello")
        self.window.menu_bar.file_menu.save_file()
        if self.window.menu_bar.file_menu.f_name != '':
            with open(self.window.menu_bar.file_menu.f_name, 'r') as f:
                self.assertEqual(f.read(), self.window.text_edit.toPlainText())
        else:
            self.assertEqual(self.window.text_edit.toPlainText(), 'hello')

    def test_new_file(self):
        self.window.text_edit.setText("hello")
        self.window.menu_bar.file_menu.new_file()
        self.assertEqual(self.window.menu_bar.file_menu.f_name, '')
        self.assertFalse(self.window.text_edit.toPlainText() == 'hello')
        self.assertEqual(self.window.text_edit.toPlainText(), '')
        self.window.text_edit.setText("hello")
        self.assertEqual(self.window.menu_bar.file_menu.f_name, '')

    def test_quit(self):
        self.window.menu_bar.file_menu.quit()
        self.assertFalse(self.window.isVisible())

    def tearDown(self):
        self.app.quit()


class EditMenuTest(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = Window()

    def test_find(self):
        self.window.text_edit.setText("- Это кто упал? Серёжа? Нет, не он, - его одёжа."
                                      " - Что же стукнула одёжа? - В середине был Серёжа.")
        self.window.menu_bar.edit_menu.find_()
        if self.window.menu_bar.edit_menu.is_find_btn_clicked:
            pos = self.window.text_edit.toPlainText().find(self.window.menu_bar.edit_menu.search_dialog.line_edit.text())
            if pos == -1:
                pass
            else:
                self.assertEqual(self.window.menu_bar.edit_menu.search_dialog.line_edit.text(),
                                 self.window.text_edit.textCursor().selectedText())

    def tearDown(self):
        self.app.quit()


if __name__ == '__main__':
    unittest.main()
