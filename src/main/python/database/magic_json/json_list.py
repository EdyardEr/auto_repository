from .delegate import Delegate
from .validation import valid_value, valid_array, valid_index_value

class JSONList(list):
    __slots__ = ('_save_to_json',)

    def __init__(self, values: dict, delegate: Delegate):
        super().__init__(values)
        self._save_to_json = delegate

    @valid_index_value
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_to_json()

    @valid_value
    def append(self, __object):
        super().append(__object)
        self._save_to_json()

    @valid_array
    def extend(self, __iterable: iter):
        super().extend(__iterable)
        self._save_to_json()

    @valid_index_value
    def insert(self, index, value):
        super().insert(index, value)
        self._save_to_json()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_to_json()

    def pop(self, __index: int = ...):
        res = super().pop(__index)
        self._save_to_json()
        return res

    def remove(self, obj):
        res = super().remove(obj)
        self._save_to_json()
        return res

    def reverse(self):
        super().reverse()
        self._save_to_json()

    def sort(self, *args, **kwargs):
        super().sort(*args, **kwargs)
        self._save_to_json()

    def clear(self):
        super().clear()
        self._save_to_json()

    def copy(self):
        raise TypeError('You can\'t copy JSONList!')
