from typing import Dict, List

from core.repository_settings.settings_file import Settings
from database.application_data import AppData


class SettingsManager:
    def __init__(self, database: AppData):
        self._database = database
        self.__git_settings_jsons: Dict[str, Settings] = {}
        self.__connect_settings()

    def add_rep(self, name: str, rep_path: str, settings: Dict[str, list]):
        self.__git_settings_jsons[name] = Settings(rep_path)
        self.update_settings(name, settings)

    def update_settings(self, name: str, settings: Dict[str, list]):
        for line in settings['ignored']:
            self.__git_settings_jsons[name].set_to_ignored(line)
        for line in settings['tracked']:
            self.__git_settings_jsons[name].set_to_ignored(line)

    def delete_rep(self, name: str):
        if name in self.__git_settings_jsons:
            del self.__git_settings_jsons[name]

    def __connect_settings(self):
        for name, path, state in self._database.get_repositories():
            if name not in self._database.get_invalid_rep_list():
                self.__git_settings_jsons[name] = Settings(path)
