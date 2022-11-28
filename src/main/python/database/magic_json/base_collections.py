import json

from .json_list import JSONList
from .json_dict import JSONDict
from .decoder import Decoder
from .delegate import Delegate


class BaseCollection:
    def __init__(self, file_path: str):
        self._path = file_path
        self._delegate = Delegate(ignore_args=True)
        self._delegate.add(self._set_to_json)
        self._delegate.add(self._init_JSON_collection)
        super().__init__(self._get_from_json(), self._delegate)

    def _init_JSON_collection(self):
        super().__init__(self._get_from_json(), self._delegate)

    def _set_to_json(self):
        with open(self._path, 'w') as write_file:
            json.dump(self, write_file, indent=4, ensure_ascii=False)

    def _get_from_json(self) -> dict:
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


class DictBaseCollection(BaseCollection, JSONDict):
    pass

class ListBaseCollection(BaseCollection, JSONList):
    pass



