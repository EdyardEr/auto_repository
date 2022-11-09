from .validator import Validator

class NewRepositoryName(Validator):
    def validation(self, name: str):
        name = name.lstrip()
        if len(name) > 20:
            return Exception('Max name length 20 symbols!')
        if not name.rstrip():
            return Exception('Can\'t contain only invisible symbols!')
        return name

