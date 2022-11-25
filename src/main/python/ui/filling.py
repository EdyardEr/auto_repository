from typing import Optional

from .window import Window

class Filling:
    def __init__(self, window: Window):
        self.window = window

    def fill_rep_path(self, text: str):
        self.window.repository_path.setText(text)

    def fill_rep_list(self, rep_list: list):
        self.window.rep_list.addItems(rep_list)

    def add_repository(self, name: str):
        self.window.rep_list.addItem(name)

    def reset_rep_list(self, rep_list: list):
        self.window.rep_list.clear()
        self.window.rep_list.addItems(rep_list)
        self.choose_rep(-1)

    def choose_rep(self, ind: int):
        self.window.rep_list.setCurrentIndex(ind)

    def switch_track_state(self, switch: bool):
        self.switch_track_light(switch)
        self.switch_button_track_name(switch)

    def switch_track_light(self, switch: bool):
        if switch:
            self.window.track_indicator.setStyleSheet('background: rgb(51,255,51);')
        else:
            self.window.track_indicator.setStyleSheet('')

    def switch_button_track_name(self, switch: bool):
        if switch:
            self.window.track_dir.setText('Track Off')
        else:
            self.window.track_dir.setText('Track On')

    def add_event_in_list(self, event: str):
        self.window.events_list.addItem(event)

    def fill_events_list(self, events_list: list):
        self.window.events_list.clear()
        if events_list is not None:
            self.window.events_list.addItems(events_list)

    def clear_events_list(self):
        self.window.events_list.clear()


