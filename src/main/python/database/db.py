from typing import List, Tuple, Dict

from database.json_data import JsonData

main_data_structure = {
    'rep_dirs': [('one', 'path_one'), ('two', 'path_two'), ('three', 'path_three')],
    'current_rep_index': 0,
}
main_db_path = r'C:\Users\ederm\Desktop\my_projects\repository\src\main\python\database\json_data.json'

class AppData:
    __slots__ = ('json_data',)

    def __init__(self):
        self.json_data = JsonData(main_db_path)

    def get_rep_names(self) -> List[str]:
        return [name for name, rep_path in self.get_repositories()]

    def get_rep_paths(self) -> List[str]:
        return [rep_path for name, rep_path in self.get_repositories()]

    def get_repositories(self) -> List[tuple]:
        return self.json_data['rep_dirs']

    def get_current_rep(self) -> Tuple[str, str]:
        return self.json_data['rep_dirs'][self.json_data['current_rep_index']]

    def get_current_rep_name(self) -> str:
        return self.get_current_rep()[0]

    def get_current_rep_path(self) -> str:
        return self.get_current_rep()[1]

    def set_current_rep_index(self, ind: int):
        self.json_data['current_rep_index'] = ind

    def get_current_rep_index(self) -> int:
        return self.json_data['current_rep_index']

    def set_new_rep(self, name, rep_path):
        self.json_data['rep_dirs'].append((name, rep_path))

    def get_reps_count(self) -> int:
        return len(self.json_data['rep_dirs'])

    def del_rep(self, name):
        for ind, rep in enumerate(self.json_data['rep_dirs']):
            if name == rep[0]:
                self.json_data['rep_dirs'].pop(ind)


if __name__ == '__main__':  # recover json data base
    path = r'json_data.json'
    data = AppData()
    answer = input('restructure Y/N? : ')
    if answer.strip() == 'Y':
        data.json_data._restructure(main_data_structure)
        print(data.json_data._get_from_json())


