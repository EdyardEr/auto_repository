def valid_value(function):
    def wrapper(self, value):
        return function(self, check_value(value))
    return wrapper

def valid_index_value(function):
    def wrapper(self, index, value):
        return function(self, index, check_value(value))
    return wrapper

def valid_array(function):
    def wrapper(self, array):
        return function(self, check_array(array))
    return wrapper

def valid_key_and_value(function):
    def wrapper(self, key, value=None):
        return function(self, check_key(key), check_value(value))
    return wrapper

def valid_dict_items(function, **kwargs):
    def wrapper(self, items):
        return function(self, check_items(items), **kwargs)
    return wrapper

def check_key(key):
    if type(key) == str:
        return key
    else:
        raise TypeError(f'Key for JSONDict can be only str! Not {type(key)}')

def check_value(value):
    if type(value) in (None, bool, int, float, str):
        return value
    elif type(value) in (tuple, list):
        return check_array(value)
    elif type(value) == dict:
        return check_items(value)
    else:
        raise TypeError(f'JSON collection can\'t keep {type(value)}!')

def check_array(array):
    return [check_value(cel) for cel in array]

def check_items(items: dict):
    return {check_key(key): check_value(value) for key, value in items.items()}
