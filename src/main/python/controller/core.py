from core.watcher import Watcher
from database.db import AppData
from threading import Thread
from typing import Dict

from ui.ui import Ui


class Core:
    def __init__(self, database: AppData, ui: Ui):
        self._database = database
        self.watchers: Dict[Watcher] = self._create_all_watchers()
        self.ui = ui

    def _create_all_watchers(self):
        return {name: Watcher(path, state) for name, path, state in self._database.get_repositories()}

    def _watchers_connect(self, func):
        for watcher in self.watchers:
            watcher.event_socket.add(func)