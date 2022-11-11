import json


class JsonData(dict):
    __slots__ = ('_path',)

    def __init__(self, db_path):
        self._path = db_path
        super().__init__(self._get_from_json())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)  # update dict
        self._set_to_json(self)          # save to json

    def _get_from_json(self):
        with open(self._path, 'r') as read_file:
            return json.load(read_file)

    def _set_to_json(self, app_data):
        with open(self._path, 'w') as write_file:
            json.dump(app_data, write_file, indent=4)

    def _restructure(self, data_structure):
        with open(self._path, 'w') as write_file:
            json.dump(data_structure, write_file)
