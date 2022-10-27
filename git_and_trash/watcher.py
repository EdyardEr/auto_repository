from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
import time


class Handler(RegexMatchingEventHandler):
    def on_any_event(self, event):
        print(event)


if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\my_projects\repository\watch_dir'
    observer = Observer()
    handler = Handler(ignore_directories=True, case_sensitive=True, ignore_regexes=[r'.*.git.*'])
    observer.schedule(handler, path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()