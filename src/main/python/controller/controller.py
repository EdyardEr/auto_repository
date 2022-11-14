from .core import Core
from .user import User
from .verifier import Verifier
from ui.ui import Ui
from database.db import AppData

class Controller:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database

        self.verifier = Verifier(self.ui, self.database)
        self.user = User(self.ui, self.database, self.verifier)
        self.core = Core(self.database, self.ui)
        self.start_application()

    def start_application(self):
        self.create_ui_links()
        self.fill_ui()

    def create_ui_links(self):
        self.ui.sockets.create_rep_button.add(self.create_new_repository)
        self.ui.sockets.del_rep_button.add(self.del_repository)
        self.ui.sockets.change_rep_combo_box.add(self.change_rep_path)
        self.ui.sockets.track_dir.add(self.track_rep)

    def track_rep(self, button_state):
        print(button_state)

    def fill_ui(self):
        """
        Here we filling ui widgets while starting.
        """
        self.fill_rep_list()

    def change_rep_path(self, line_ind):
        self.database.set_current_rep_index(line_ind)
        if line_ind != -1:
            text = self.database.get_current_rep_path()
        else:
            text = ''
        self.ui.filling.fill_rep_path(text)

    def create_new_repository(self, *button_state):
        new_path = self.user.choose_rep_path()
        if new_path is None:
            return
        new_name = self.user.write_rep_name()
        if new_name is None:
            return
        self.save_and_actual_rep(new_name, new_path)

    def del_repository(self, *button_state):
        name = self.user.del_repository()
        if name is None:
            return
        self.database.del_rep(name)
        self.ui.window.rep_list.setCurrentIndex(-1)
        self.fill_rep_list()

    def save_and_actual_rep(self, new_name, new_path):
        self.database.set_new_rep(new_name, new_path)
        ind = self.database.get_reps_count() - 1
        self.ui.filling.fill_rep_list(self.database.get_rep_names(), ind)

    def fill_rep_list(self):
        ind = self.database.get_current_rep_index()
        self.ui.filling.fill_rep_list(self.database.get_rep_names(), ind)

