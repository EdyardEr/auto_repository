import os
import time
from threading import Thread


class PathChecker:
    __slots__ = ('_path', '_exception_run', '_time_interval')

    def __init__(self, path: str, socket: callable, time_interval: int):
        self._path = path
        self._exception_run = socket
        self._time_interval = time_interval
        if self._path_check():
            self._start()
        else:
            self._exception_run()

    def _start(self):
        thread = Thread(target=self._loop)
        thread.start()

    def _loop(self):
        while True:
            if not self._path_check():
                self._exception_run()
                return
            time.sleep(self._time_interval)

    def _path_check(self):
        return os.path.exists(self._path)