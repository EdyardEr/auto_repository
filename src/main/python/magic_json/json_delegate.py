class Delegate:
    __slots__ = ('_ignore_args', '_subscribers')

    def __init__(self, ignore_args=False):
        self._subscribers = list()
        self._ignore_args = ignore_args

    def __call__(self, *args, **kwargs):
        for subscriber in self._subscribers:
            if self._ignore_args:
                self._call_without_args(subscriber)
            else:
                self._call_with_args(*args, **kwargs)

    def add(self, subscriber: callable):
        self._subscribers.append(subscriber)

    def clear(self):
        self._subscribers.clear()

    @staticmethod
    def _call_without_args(subscriber: callable):
        subscriber()

    @staticmethod
    def _call_with_args(subscriber: callable, *args, **kwargs):
        subscriber(*args, **kwargs)