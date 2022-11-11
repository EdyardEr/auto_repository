from .extension import Window

class Filling:
    def __init__(self, window: Window):
        self.window = window

    def fill_rep_path(self, text: str):
        self.window.repository_path.setText(text)

    def fill_rep_list(self, rep_list: list):
        self.window.rep_list.clear()
        self.window.rep_list.addItems(rep_list)
