from core.watcher import Watcher
from database.db import AppData
from typing import Dict
from ui.ui import Ui


class Core:
    def __init__(self, database: AppData, ui: Ui):
        self._database = database
        # self._watchers = self._create_all_watchers()
        # self._watchers_connect_exception()
        # self._start_watchers()

        self.ui = ui

    def _create_all_watchers(self) -> Dict[str, Watcher]:
        return {name: Watcher(path, state) for name, path, state in self._database.get_repositories()}

    def watchers_connect(self, func):
        for watcher in self._watchers.values():
            watcher.event_socket.add(func)

    def _watchers_connect_exception(self):
        for name, watcher in self._watchers.items():
            watcher.except_path_socket.add(self._set_track_state_for(name, False))

    def _set_track_state_for(self, name, state):
        def func():
            print(name, state)
            self._database.set_rep_track_state(name, state)
        return func

    def _start_watchers(self):
        for name, watcher in self._watchers.items():
            if self._database.get_rep_track_state(name):
                watcher.start()

    def turn_on_watcher(self, name):
        self._watchers[name].start()

    def turn_off_watcher(self, name):
        self._watchers[name].stop()