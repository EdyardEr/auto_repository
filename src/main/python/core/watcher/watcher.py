from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

from typing import Optional

from core.watcher.path_checker import PathChecker
from delegate import Delegate


class Handler(RegexMatchingEventHandler):
    __slots__ = ('delegate',)

    def __init__(self, delegate):
        self.delegate = delegate
        super().__init__(ignore_directories=True, case_sensitive=True, ignore_regexes=[r'.*.git.*'])

    def on_any_event(self, event):
        self.delegate(event)

class Watcher:
    __slots__ = ('_path', '_observer', '_path_checker', '_handler', 'sockets')

    def __init__(self, dir_path: str):
        self.sockets = {
            'events': Delegate(),
            'path_exception': Delegate()

        }
        self.sockets['path_exception'].add(self.stop)

        self._path = dir_path
        self._observer: Optional[Observer] = None
        self._path_checker = PathChecker(self._path, self.sockets['path_exception'], 1)
        self._handler = Handler(self.sockets['events'])

    def _create_observer_thread(self):
        self._observer = Observer()
        self._observer.schedule(self._handler, path=self._path, recursive=True)

    def start(self):
        if self._path_checker.start():
            print(f'started: {self._path}')
            self._create_observer_thread()
            self._observer.start()
        else:
            print(f'can not start: {self._path}')

    def stop(self):
        if self._observer is not None:
            print(f'stopped: {self._path}')
            self._observer.stop()
            self._path_checker.stop()
        else:
            print(f'can not stop: {self._path}')

