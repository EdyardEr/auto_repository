class Event(set):
    __slots__ = ()

    def __call__(self, *args, **kwargs):
        for delegate in self:
            delegate(*args, **kwargs)


if __name__ == '__main__':
    pass

