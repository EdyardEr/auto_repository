from typing import List, Tuple, Dict, Union

from database.magic_json.interface import JSON

json_recover_data = {
    'tracked': [],
    'ignored': [],
}

data_structure = Dict[
    str, List[str]
]

class Settings:
    __slots__ = ('__json_data',)

    def __init__(self, rep_path: str):
        path_into_rep_dir = '/.git/info/settings.json'
        path = rep_path + path_into_rep_dir
        try:
            self.__json_data: data_structure = JSON.connection(path)
        except FileNotFoundError:
            self.__json_data: data_structure = JSON.create(path, dict)
            self.__json_data['tracked'] = list()
            self.__json_data['ignored'] = list()

    def set_to_tracked(self, line: str):
        self.__json_data['tracked'].append(line)

    def set_to_ignored(self, line: str):
        self.__json_data['ignored'].append(line)

    def del_tracked(self, line: str):
        self.__json_data['tracked'].remove(line)

    def del_ignored(self, line: str):
        self.__json_data['ignored'].remove(line)

    def get_tracked_list(self):
        return self.__json_data['tracked']

    def get_ignored_list(self):
        return self.__json_data['ignored']


if __name__ == '__main__':
    settings = Settings(r'C:/Users/ederm/Desktop/test_dir')
    settings.del_ignored('.git')
    settings.del_tracked('tracked')
    print(settings.get_tracked_list())
    print(settings.get_ignored_list())

