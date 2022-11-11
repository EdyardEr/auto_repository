from typing import Tuple

from .validator import Validator

class NewRepositoryName(Validator):
    def validation(self, args: Tuple[str, bool]):
        name, is_actual = args
        if is_actual:
            name = name.lstrip()
            if len(name) > 20:
                name = Exception('Max name length 20 symbols!')
            if not name.rstrip():
                name = Exception('Can\'t contain only invisible symbols!')
        return name, is_actual

