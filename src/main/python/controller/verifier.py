from database.db import AppData
from ui.ui import Ui


class Verifier:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database

    def is_path_exist(self, path) -> bool:
        paths: list = self.database.get_rep_paths()
        return True if path in paths else False