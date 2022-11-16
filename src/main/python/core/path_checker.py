import os
import time
from threading import Thread
from typing import Optional


class PathChecker:
    __slots__ = ('_path', '_exception_run', '_time_interval', '_thread')

    def __init__(self, path: str, exception_func: callable, time_interval: int):
        self._path = path
        self._exception_run = exception_func
        self._time_interval = time_interval
        self._thread: Optional[Thread] = None

    def start(self) -> bool:
        if self._path_check():
            self._thread = Thread(target=self._loop)
            self._thread.start()
            return True
        else:
            self._exception_run()
            return False

    def stop(self):
        self._thread = None

    def _loop(self):
        while self._thread is not None:
            if not self._path_check():
                self._exception_run()
                self.stop()
            time.sleep(self._time_interval)

    def _path_check(self) -> bool:
        return os.path.exists(self._path)