from .delegate import Delegate
from .validation import valid_key_and_value, valid_dict_items

class JSONDict(dict):
    __slots__ = ('_save_to_json',)

    def __init__(self, values: dict, delegate: Delegate):
        super().__init__(values)
        self._save_to_json = delegate

    @valid_key_and_value
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_to_json()

    @valid_key_and_value
    def setdefault(self, key, value=None):
        super().setdefault(key, value)
        self._save_to_json()

    @valid_dict_items
    def update(self, __m, **kwargs):
        super().update(__m, **kwargs)
        self._save_to_json()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_to_json()

    def pop(self, key):
        super().pop(key)
        self._save_to_json()

    def clear(self):
        super().clear()
        self._save_to_json()

    def popitem(self):
        result = super().popitem()
        self._save_to_json()
        return result

    def copy(self):
        raise TypeError('You can\'t copy JSONDict!')

