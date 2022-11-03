import json


data_structure = {
    'rep_dirs': {'key1': 1},
    'jdshf': {},
}

class AppData(dict):
    __slots__ = ()

    def __init__(self):
        super().__init__(self._get_from_json())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)  # update dict
        self._set_to_json(self)          # save to json

    def _get_from_json(self):
        with open('json_data.json', 'r') as read_file:
            return json.load(read_file)

    def _set_to_json(self, app_data):
        with open('json_data.json', 'w') as write_file:
            json.dump(app_data, write_file, indent=4)
    #
    # def _recovery(self):
    #     with open('json_data.json', 'w') as write_file:
    #         json.dump(data_structure, write_file)


if __name__ == '__main__':
    # f = data_structure['rep_dirs'].pop()  # нужно чтобы self видел структуру
    # print(f)
    data = AppData()
    data['jdshf'] = 777
    print(data)


