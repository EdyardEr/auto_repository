from core.watcher import Watcher
from database.application_data import AppData
from typing import Dict
from ui.ui import Ui


class WatcherManager:
    def __init__(self, database: AppData, ui: Ui):
        self._database = database
        self.ui = ui
        self.__watchers: Dict[str, Watcher] = {}
        self.__events_lists: Dict[str, list] = {}

        self.__create_watchers()
        self.__create_events_lists()
        self.__define_watchers_sockets()
        self.__start_watchers()

    def __create_events_lists(self):
        self.__events_lists = {name: list() for name in self.__watchers.keys()}
        # self._events_lists = dict.fromkeys(self._watchers, list())

    def add_new_watcher(self, name: str, path: str):
        self.__watchers[name] = Watcher(path)
        self.__events_lists[name] = list()

    def __create_watchers(self):
        self.__watchers.update({name: Watcher(path) for name, path, state in self._database.get_repositories()})

    def __define_watchers_sockets(self):
        for name, watcher in self.__watchers.items():
            watcher.sockets['events'].add(self.__add_new_event(name))
            watcher.sockets['path_exception'].add(self.__change_watcher_state(name))

    def exception_sockets_add(self, function: callable):
        for name, watcher in self.__watchers.items():
            watcher.sockets['path_exception'].add(function)

    def events_sockets_add(self, function: callable):
        for name, watcher in self.__watchers.items():
            watcher.sockets['events'].add(function)

    def __start_watchers(self):
        for name, watcher in self.__watchers.items():
            if self._database.get_rep_track_state(name):
                watcher.start()

    def turn_on_watcher(self, name):
        self._database.set_rep_track_state(name, True)
        self.ui.filling.switch_track_indicator(True)
        self.__watchers[name].start()

    def turn_off_watcher(self, name):
        self._database.set_rep_track_state(name, False)
        self.ui.filling.switch_track_indicator(False)
        self.__watchers[name].stop()

    def __change_watcher_state(self, name):
        def func():
            print(f'{name}: fake exception func')
            self.turn_off_watcher(name)
            self.ui.window.show_warning_mess('Repository path incorrect!!!')
        return func

    def __add_new_event(self, name):
        def func(event):
            text_to_list = self.__format_event_text(event)
            self.__events_lists[name].append(text_to_list)
            if name == self._database.get_current_rep_name():
                self.ui.filling.add_event_in_list(text_to_list)
        return func

    @staticmethod
    def __format_event_text(event):
        path = event.src_path[event.src_path.find('\\'):]
        return f'{event.event_type} - ...{path}'

    def get_current_events_list(self):
        return self.__events_lists[self._database.get_current_rep_name()]
