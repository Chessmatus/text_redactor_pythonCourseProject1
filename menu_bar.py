from file_menu import FileMenu
from edit_menu import EditMenu
from view_menu import ViewMenu
from PyQt5.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, window_):
        super().__init__()

        self.window = window_

        self.file_menu = FileMenu(self)
        self.addMenu(self.file_menu)

        self.edit_menu = EditMenu(self)
        self.addMenu(self.edit_menu)

        self.view_menu = ViewMenu(self)
        self.addMenu(self.view_menu)
