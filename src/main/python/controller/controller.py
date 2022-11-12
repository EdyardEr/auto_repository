from .user import User
from .verifier import Verifier
from ui.ui import Ui
from database.db import AppData

class Controller:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database

        self.verifier = Verifier(self.ui, self.database)
        self.user = User(self.ui, self.verifier)

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
        new_path = self.user.choose_rep_path()
        if new_path is None:
            return
        new_name = self.user.write_rep_name()
        if new_name is None:
            return
        self.save_and_actual_rep(new_name, new_path)

    def save_and_actual_rep(self, new_name, new_path):
        self.database.set_new_rep(new_name, new_path)
        ind = self.database.get_reps_count()
        self.ui.filling.fill_rep_list(self.database.get_rep_names(), ind)

