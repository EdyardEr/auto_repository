import os
from typing import Optional


class Gitignore:
    def __init__(self, dir_path: str = ''):
        self.__dir_path = dir_path

    def create(self):
        with open(self.__dir_path + '\.gitignore', 'w+'):
            pass

    def delete(self):
        try:
            os.remove(self.__dir_path + r'\.gitignore')
            return True
        except FileNotFoundError:
            return False