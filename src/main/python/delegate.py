class Delegate(set):
    __slots__ = ('_ignore_args',)

    def __init__(self, ignore_args=False):
        super().__init__(self)
        self._ignore_args = ignore_args

    def __call__(self, *args, **kwargs):
        if self._ignore_args:
            self._call_without_args()
        else:
            for delegate in self:
                delegate(*args, **kwargs)

    def _call_without_args(self):
        for delegate in self:
            delegate()