from PyQt5.QtCore import QCoreApplication

from .extension import Window
from event import Event

class Filling:
    def __init__(self, window: Window):
        self.window = window

    def fill_rep_path(self, text):
        self.window.repository_path.setText(text)

    def fill_rep_list(self, rep_list: list):
        self.window.rep_list.clear()
        self.window.rep_list.addItems(rep_list)