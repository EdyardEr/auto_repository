from typing import Optional

from .window import Window

class Filling:
    def __init__(self, window: Window):
        self.window = window

    def fill_rep_path(self, text: str):
        self.window.repository_path.setText(text)

    def fill_rep_list(self, rep_list: list, ind: Optional[int] = None):
        self.window.rep_list.clear()
        self.window.rep_list.addItems(rep_list)
        if ind is not None:
            self.window.rep_list.setCurrentIndex(ind)

