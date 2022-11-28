from typing import List, Tuple, Dict, Union

from database.magic_json.interface import JSON

json_recover_data = {
    'rep_dirs': [('one', 'path_one', False), ('two', 'path_two', False), ('three', 'path_three', False)],
    'current_rep_index': 0,
}

data_structure = Dict[
    str, Union[
        int,
        List[Union[list, tuple]],
    ]
]

main_db_path = r'C:\Users\ederm\Desktop\my_projects\repository\src\main\python\database\json_data.json'

class AppData:
    __slots__ = ('__json_data', '__invalid_repositories')

    def __init__(self):
        self.__json_data: data_structure = JSON.connection(main_db_path)
        self.__invalid_repositories = list()

    def get_invalid_rep_list(self) -> List[str]:
        return self.__invalid_repositories

    def get_rep_names(self) -> List[str]:
        return [name for name, rep_path, track_state in self.get_repositories()]

    def get_rep_paths(self) -> List[str]:
        return [rep_path for name, rep_path, track_state in self.get_repositories()]

    def get_repositories(self) -> List[Tuple[str, str, bool]]:
        return self.__json_data['rep_dirs']

    def get_current_rep(self) -> Tuple[str, str]:
        return self.__json_data['rep_dirs'][self.__json_data['current_rep_index']]

    def get_current_rep_name(self) -> str:
        return self.get_current_rep()[0]

    def get_current_rep_track_state(self) -> bool:
        return self.get_current_rep()[2]

    def get_current_rep_path(self) -> str:
        return self.get_current_rep()[1]

    def set_current_rep_index(self, ind: int):
        self.__json_data['current_rep_index'] = ind

    def get_rep_track_state(self, name: str):
        for current_name, path, state in self.__json_data['rep_dirs']:
            if current_name == name:
                return state

    def set_invalid_rep(self, name: str):
        self.__invalid_repositories.append(name)

    def set_rep_track_state(self, name: str, state: bool):
        for ind, rep in enumerate(self.__json_data['rep_dirs']):
            if name == rep[0]:
                self.__json_data['rep_dirs'][ind][2] = state

    def get_current_rep_index(self) -> int:
        return self.__json_data['current_rep_index']

    def set_new_rep(self, name: str, rep_path: str, track: bool):
        self.__json_data['rep_dirs'].append([name, rep_path, track])

    def get_reps_count(self) -> int:
        return len(self.__json_data['rep_dirs'])

    def del_rep(self, name):
        for ind, rep in enumerate(self.__json_data['rep_dirs']):
            if name == rep[0]:
                self.__json_data['rep_dirs'].pop(ind)


if __name__ == '__main__':  # recover json data base
    path = r'json_data.json'
    data = AppData()
    answer = input('restructure Y/N? : ')
    if answer.strip() == 'Y':
        data.__json_data._restructure(json_recover_data)
        print(data.__json_data._get_from_json())


