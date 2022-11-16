from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from core.os_path_checker import PathChecker
from ui.delegate import Delegate
from typing import Optional

class Handler(RegexMatchingEventHandler):
    __slots__ = ('delegate',)

    def __init__(self, delegate):
        self.delegate = delegate
        super().__init__(ignore_directories=True, case_sensitive=True, ignore_regexes=[r'.*.git.*'])

    def on_any_event(self, event):
        self.delegate(event)

class Watcher:
    __slots__ = ('_path', '_state', '_observer', 'event_socket', 'except_path_socket',
                 '_path_checker', '_handler', '_correct_path')

    def __init__(self, path: str, state: bool):
        self._path = path
        self._state = state
        self._observer: Optional[Observer] = None

        self.event_socket = Delegate()
        self.except_path_socket = Delegate()

        self.except_path_socket.add(self._path_incorrect)
        self._path_checker = PathChecker(self._path, self.except_path_socket, 1)
        self._correct_path = True
        self._handler = Handler(self.event_socket)

    def _path_incorrect(self):
        self._correct_path = False

    def _create_observer_thread(self):
        self._observer = Observer()
        self._observer.schedule(self._handler, path=self._path, recursive=True)

    def stop(self):
        print(f'stoped: {self._path}')
        self._state = False
        if self._observer is not None:
            self._observer.stop()
            self._path_checker.stop()

    def start(self):
        self._path_checker.start()
        if self._correct_path:
            print(f'started: {self._path}')
            self._state = True
            self._create_observer_thread()
            self._observer.start()
        else:
            self.stop()



if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\lol'

    def test_func(event):
        print(event)


    watcher = Watcher(path, True)
    watcher.event_socket.add(test_func)
    while True:
        pass
