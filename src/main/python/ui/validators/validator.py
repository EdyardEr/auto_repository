from functools import wraps
from typing import Callable

class Validator:
    __slots__ = ()

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.validation(result)
        return wrapper

    def validation(self, result):
        raise NotImplementedError('validation method not implemented!')