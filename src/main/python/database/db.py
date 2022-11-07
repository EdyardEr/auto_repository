import json


data_structure = {
    'rep_dirs': {'name': 'path', 'two': 8795689},  # name: str, path: str
}

path = r'database/json_data.json'

class AppData(dict):
    __slots__ = ()

    def __init__(self):
        super().__init__(self._get_from_json())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)  # update dict
        self._set_to_json(self)          # save to json

    def _get_from_json(self):
        with open(path, 'r') as read_file:
            return json.load(read_file)

    def _set_to_json(self, app_data):
        with open(path, 'w') as write_file:
            json.dump(app_data, write_file, indent=4)

    def recovery(self):
        with open(path, 'w') as write_file:
            json.dump(data_structure, write_file)


if __name__ == '__main__':
    path = r'json_data.json'
    data = AppData()
    data.recovery()
    print(data._get_from_json())


