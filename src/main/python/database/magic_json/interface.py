import json

from .base_collections import DictBaseCollection, ListBaseCollection


class JSON:
    __slots__ = ()
    __collection_types = {
        dict: DictBaseCollection,  # стоит так делать? или лучше по str ключам
        list: ListBaseCollection
    }

    @classmethod
    def connection(cls, file_path: str):
        return cls.__collection_types[cls.__define_collection_type(file_path)](file_path)

    @classmethod
    def create(cls, file_path: str, collection_type: type):
        cls.__create(file_path, collection_type)
        return cls.__collection_types[collection_type](file_path)  # как нормально зааннотировать?

    @staticmethod
    def __define_collection_type(file_path: str) -> type:
        with open(file_path, 'r') as read_file:
            return type(json.load(read_file))

    @staticmethod
    def __create(file_path: str, collection_type: type):
        with open(file_path, 'w') as write_file:
            json.dump(collection_type(), write_file, indent=4)

