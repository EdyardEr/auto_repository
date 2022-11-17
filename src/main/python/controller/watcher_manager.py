from core.watcher import Watcher
from database.db import AppData
from typing import Dict
from ui.ui import Ui


def fake_event_func(name):
    def func(event):
        print(f'{name}: {event}')
    return func

def fake_exception_func(name):
    def func():
        print(f'{name}: fake exception func')
    return func

class WatcherManager:
    def __init__(self, database: AppData, ui: Ui):
        self._database = database
        self.ui = ui
        self._watchers: Dict[str, Watcher] = {}

        self._create_watchers()
        self._define_watchers_sockets()
        self._start_watchers()

    def _create_watchers(self):
        self._watchers.update({name: Watcher(path) for name, path, state in self._database.get_repositories()})

    def _define_watchers_sockets(self):
        for name, watcher in self._watchers.items():
            watcher.sockets['events'].add(fake_event_func(name))
            watcher.sockets['path_exception'].add(fake_exception_func(name))

    def _start_watchers(self):
        for name, watcher in self._watchers.items():
            if self._database.get_rep_track_state(name):
                watcher.start()

    # def turn_on_watcher(self, name):
    #     self._watchers[name].start()
    #
    # def turn_off_watcher(self, name):
    #     self._watchers[name].stop()