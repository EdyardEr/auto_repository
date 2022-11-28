from core.git.git import Git
from database.application_data import AppData
from typing import Dict
from ui.ui import Ui


class GitManager:
    def __init__(self, database: AppData, ui: Ui):
        self._database = database
        self.ui = ui
        self.__git_repositories: Dict[str, Git] = {}
        self.__create_git_connection()
        self.__check_repositories()

    def add_rep(self, name: str, path: str):
        self.__git_repositories[name] = Git(path)
        self.__git_repositories[name].delete_repository()
        self.__git_repositories[name].create_repository()

    def delete_rep(self, name: str):
        self.__git_repositories[name].delete_repository()
        del self.__git_repositories[name]

    def __create_git_connection(self):
        self.__git_repositories.update({name: Git(path) for name, path, state in self._database.get_repositories()})

    def __check_repositories(self):
        for name, git in self.__git_repositories.items():
            if not git.is_valid():
                self._database.set_invalid_rep(name)
                self.ui.window.show_invalid_repository(name)


