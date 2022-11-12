from ui.ui import Ui
from database.db import AppData

class Controller:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database
        self.create_ui_links()
        self.fill_ui()

    def create_ui_links(self):
        self.ui.sockets.create_rep_button.add(self.create_new_repository)
        self.ui.sockets.change_rep_combo_box.add(self.change_rep_path)

    def fill_ui(self):
        """
        Here we filling ui widgets while starting.
        """
        ind = self.database.get_current_rep_index()
        self.ui.filling.fill_rep_list(self.database.get_rep_names(), ind)

    def change_rep_path(self, line_ind):
        self.database.set_current_rep_index(line_ind)
        self.ui.filling.fill_rep_path(self.database.get_current_rep_path())

    def create_new_repository(self, *button_state):
        new_path = self.ui.window.request_dir_path()
        if self.is_path_exist(new_path):
            self.valid_error('Repository in this directory already exist!')
            return
        if not new_path:
            return
        new_name, is_actual = self.ui.window.request_repository_name()
        if not is_actual:
            return
        if type(new_name) == Exception:
            self.valid_error(new_name)
        else:
            self.database.set_new_rep(new_name, new_path)
            ind = self.database.get_reps_count()
            self.ui.filling.fill_rep_list(self.database.get_rep_names(), ind)

    def is_path_exist(self, path) -> bool:
        paths: list = self.database.get_rep_paths()
        return True if path in paths else False

    def valid_error(self, exception):
        self.ui.window.show_validator_except_mess(str(exception))
