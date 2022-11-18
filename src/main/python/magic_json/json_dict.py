from json_delegate import Delegate
from validation import valid_key_and_value, valid_dict_items

class JSONDict(dict):
    __slots__ = ('_save_to_json',)

    def __init__(self, values: dict, delegate: Delegate):
        super().__init__(values)
        self._save_to_json = delegate

    @valid_key_and_value
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_to_json()
        print('setitem')

    @valid_key_and_value
    def setdefault(self, key, value=None):
        super().setdefault(key, value)
        self._save_to_json()
        print(f'setdefault k:{key} v:{value}')

    @valid_dict_items
    def update(self, __m, **kwargs):
        super().update(__m, **kwargs)
        self._save_to_json()
        print(f'update --m:{__m}')

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_to_json()
        print('delitem')

    def pop(self, key):
        super().pop(key)
        self._save_to_json()
        print('pop')

    def clear(self):
        super().clear()
        self._save_to_json()
        print('clear')

    def popitem(self):
        result = super().popitem()
        self._save_to_json()
        print('popitem')
        return result

    def copy(self):
        raise TypeError('You can\'t copy JSONDict!')


# if __name__ == '__main__':
#     def my_print():
#         print('save')
#
#     my_dict = JSONDict({'sdf': []}, my_print)
#     {}.copy()
#     print(my_dict)
