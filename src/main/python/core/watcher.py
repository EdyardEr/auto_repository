from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
import time

from ui.delegate import Delegate

class Handler(RegexMatchingEventHandler):
    def on_any_event(self, event):
        print(event)

class Watcher:
    def __init__(self, path=None):
        self.socket = Delegate()
        self._path = path
        self._observer = Observer()
        self._handler = Handler(ignore_directories=True, case_sensitive=True, ignore_regexes=[r'.*.git.*'])
        if path is not None:
            self._set_handler(path)

    def _set_handler(self, path: str):
        self._observer.schedule(self._handler, path=path, recursive=True)

    def path(self, path: str):
        self.stop()
        self._set_handler(path)
        self.start()

    def start(self):
        self._observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
        self._observer.join()

    def stop(self):
        self._observer.stop()


if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\Детали'
    watcher = Watcher(path)
    watcher.start()
