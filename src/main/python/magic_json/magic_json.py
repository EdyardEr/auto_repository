import json

from json_list import JSONList
from json_dict import JSONDict
from json_decoder import Decoder
from json_delegate import Delegate


class JsonData(JSONDict):
    __slots__ = ('_path', '_delegate')

    def __init__(self, path_to_json: str):
        self._path = path_to_json
        self._delegate = Delegate(ignore_args=True)
        self._delegate.add(self._set_to_json)
        self._delegate.add(self._init_JSON_collection)
        super().__init__(self._get_from_json(), self._delegate)

    def _init_JSON_collection(self):
        super().__init__(self._get_from_json(), self._delegate)

    def _set_to_json(self):
        print('запись')
        with open(self._path, 'w') as write_file:
            json.dump(self, write_file, indent=4)

    def _get_from_json(self) -> dict:
        print('чтение')
        with open(self._path, 'r') as read_file:
            return json.load(
                read_file,
                cls=Decoder,
                array_hook=self._make_list(self._delegate),
                object_hook=self._make_dict(self._delegate)
            )

    @staticmethod
    def _make_dict(delegate):
        def func(values) -> dict:
            return JSONDict(values, delegate)
        return func

    @staticmethod
    def _make_list(delegate):
        def func(values) -> list:
            return JSONList(values, delegate)
        return func


if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\my_projects\repository\data.json'
    j = JsonData(path)
    j = []
    d = dict()
    print(j)
    del j['12'][0]
    print(j)


