from delegate import Delegate
from validation import valid_key_and_value, valid_value, valid_array, valid_index_value

class JSONList(list):
    __slots__ = ('_save_to_json',)

    def __init__(self, values: dict, delegate: Delegate):
        super().__init__(values)
        self._save_to_json = delegate

    @valid_index_value
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_to_json()
        print('getitem')

    @valid_value
    def append(self, __object):
        super().append(__object)
        self._save_to_json()
        print(f'append {__object}')

    @valid_array
    def extend(self, __iterable: iter):
        super().extend(__iterable)
        self._save_to_json()
        print('extend')

    @valid_index_value
    def insert(self, index, value):
        super().insert(index, value)
        self._save_to_json()
        print('insert')

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_to_json()
        print('delitem')

    def pop(self, __index: int = ...):
        res = super().pop(__index)
        self._save_to_json()
        print('pop')
        return res

    def remove(self, obj):
        res = super().remove(obj)
        self._save_to_json()
        print('remove')
        return res

    def reverse(self):
        super().reverse()
        self._save_to_json()
        print('reverse')

    def sort(self, *args, **kwargs):
        super().sort(*args, **kwargs)
        self._save_to_json()
        print('sort')

    def clear(self):
        super().clear()
        self._save_to_json()
        print('clear')

    def copy(self):
        raise TypeError('You can\'t copy JSONList!')


# if __name__ == '__main__':
#     def my_print():
#         print('save')
#     my_list = JSONList([1, 2], my_print)
#     # {}.copy()
#
#     # [].copy()
#     # my_list.append({1, 3})
#     # my_list.clear()
#     # my_list.pop(0)
#     # [].count()
#     # my_list.extend({{3: 3}, 3})
#     # my_list.reverse()
#     # my_list.insert()
#     # my_list.index(1)
#     # my_list.remove(4)
#     # [].sort()
#     print(my_list)