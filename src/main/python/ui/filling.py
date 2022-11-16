from typing import Optional

from .window import Window

class Filling:
    def __init__(self, window: Window):
        self.window = window

    def fill_rep_path(self, text: str):
        self.window.repository_path.setText(text)

    def fill_tracker_tab(self, rep_list: list, index: int, track: bool):
        self.fill_rep_list(rep_list)
        self.choose_rep(index)
        self.track_indicate_light(track)

    def fill_rep_list(self, rep_list: list):
        self.window.rep_list.clear()
        self.window.rep_list.addItems(rep_list)

    def choose_rep(self, ind: int):
        self.window.rep_list.setCurrentIndex(ind)

    def track_indicate_light(self, switch: bool):
        if switch:
            self.window.track_indicator.setStyleSheet('background: rgb(51,255,51);')
        else:
            self.window.track_indicator.setStyleSheet('')


