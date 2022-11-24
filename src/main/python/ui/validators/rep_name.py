from typing import Tuple

from .validator import Validator

class NewRepositoryName(Validator):
    def validation(self, args: Tuple[str, bool]):
        name, is_actual = args
        if is_actual:
            name = name.lstrip()
            max_len = 40
            if len(name) > max_len:
                name = Exception(f'Max name length {max_len} symbols!')
            if not name.rstrip():
                name = Exception('Can\'t contain only invisible symbols!')
        return name, is_actual

