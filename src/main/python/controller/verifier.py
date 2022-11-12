from database.db import AppData
from ui.ui import Ui


class Verifier:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database

    def is_path_exist(self, path) -> bool:
        paths: list = self.database.get_rep_paths()
        return True if path in paths else False

    def is_name_exist(self, name) -> bool:
        names: list = self.database.get_rep_names()
        return True if name in names else False

    def valid_error(self, exception):
        self.ui.window.show_validator_except_mess(str(exception))