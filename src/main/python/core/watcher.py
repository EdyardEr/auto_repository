from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from core.os_path_checker import PathChecker
from ui.delegate import Delegate

class Handler(RegexMatchingEventHandler):
    __slots__ = ('delegate',)

    def __init__(self, delegate):
        self.delegate = delegate
        super().__init__(ignore_directories=True, case_sensitive=True, ignore_regexes=[r'.*.git.*'])

    def on_any_event(self, event):
        self.delegate(event)

class Watcher:
    __slots__ = ('_path', '_state', '_observer', 'event_socket', 'except_path_socket',
                 '_path_checker', '_handler')

    def __init__(self, path: str, state: bool):
        self._path = path
        self._state = state
        self._observer = Observer()

        self.event_socket = Delegate()
        self.except_path_socket = Delegate()

        self.except_path_socket.add(self.stop)
        self._path_checker = PathChecker(path, self.except_path_socket, 1)

        self._handler = Handler(self.event_socket)
        self._observer.schedule(self._handler, path=self._path, recursive=True)
        if self._state:
            self.start()

    def stop(self):
        print(f'stoped: {self._path}')
        self._state = False
        self._observer.stop()

    def start(self):
        print(f'started: {self._path}')
        self._state = True
        self._observer.start()


if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\lol'

    def test_func(event):
        print(event)


    watcher = Watcher(path, True)
    watcher.event_socket.add(test_func)
    while True:
        pass
