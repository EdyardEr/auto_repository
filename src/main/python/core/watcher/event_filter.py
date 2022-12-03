import os.path
from typing import Dict


class EventFilter:
    __slots__ = ('__settings', '__path')

    def __init__(self, path: str, settings: Dict[str, list]):
        self.__settings = settings
        self.__path = self.__to_norm_list(path)

    def check(self, event) -> bool:
        if self.__settings['tracked']:
            tracked = any([self.__check(event.src_path, line) for line in self.__settings['tracked']])
        else:
            tracked = True
        if self.__settings['ignored']:
            ignored = not any([self.__check(event.src_path, line) for line in self.__settings['ignored']])
        else:
            ignored = True
        return all((tracked, ignored))

    def __check(self, path: str, line: str):
        event_path = self.__to_norm_list(path)
        if not self.__is_paths_match(event_path, self.__path):
            raise FileNotFoundError('Incorrect path!!!')
        else:
            increment_event_path = event_path[len(self.__path):]
            line = self.__to_norm_list(line)
            if self.__is_paths_match(increment_event_path, line):
                return True
            elif len(line) == 1:
                if self.__is_file_or_dir_match(increment_event_path, line[0]):
                    return True
                elif line[0].split('.')[-1] == increment_event_path[-1].split('.')[-1]:
                    return True

    @staticmethod
    def __is_file_or_dir_match(path: list, name):
        for dir_or_file_name in path:
            if dir_or_file_name == name:
                return True
        return False

    @staticmethod
    def __is_paths_match(biggest_path: list, sub_path: list):
        if biggest_path[:len(sub_path)] == sub_path:
            return True
        else:
            return False

    def is_extension_match(self):
        pass

    @staticmethod
    def __to_norm_list(path: str) -> list:
        norm_path = os.path.normpath(path)
        norm_list = norm_path.split('\\')
        return norm_list

