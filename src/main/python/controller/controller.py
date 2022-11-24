from .watcher_manager import WatcherManager
from .user import User
from .verifier import Verifier
from ui.ui import Ui
from database.application_data import AppData

class Controller:
    def __init__(self, ui: Ui, database: AppData):
        self.ui = ui
        self.database = database

        self.verifier = Verifier(self.ui, self.database)
        self.user = User(self.ui, self.database, self.verifier)
        self.core = WatcherManager(self.database, self.ui)
        self.start_application()

    def start_application(self):
        self.create_ui_links()
        self.fill_ui()

    def create_ui_links(self):
        self.ui.sockets.create_rep_button.add(self.create_new_repository)
        self.ui.sockets.del_rep_button.add(self.del_repository)
        self.ui.sockets.change_rep_combo_box.add(self.change_rep)
        self.ui.sockets.track_dir.add(self.track_rep)

    def track_rep(self, button_state):   # do refactoring !!!
        current_name = self.database.get_current_rep_name()
        if self.database.get_current_rep_state():
            # self.core.turn_off_watcher(current_name)
            self.database.set_rep_track_state(current_name, False)
            self.ui.filling.track_indicate_light(False)
        else:
            # self.core.turn_on_watcher(current_name)
            self.database.set_rep_track_state(current_name, True)
            self.ui.filling.track_indicate_light(True)

    def fill_ui(self):
        """
        Here we filling ui widgets while starting.
        """
        self.fill_rep_list()

    def change_rep(self, line_ind):
        self.database.set_current_rep_index(line_ind)
        if line_ind != -1:
            text = self.database.get_current_rep_path()
            track_state = self.database.get_current_rep_state()
        else:
            text = ''
            track_state = False
        self.ui.filling.fill_rep_path(text)
        self.ui.filling.track_indicate_light(track_state)

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
        self.database.set_new_rep(new_name, new_path, False)
        ind = self.database.get_reps_count() - 1
        self.ui.filling.fill_tracker_tab(self.database.get_rep_names(), ind, False)

    def fill_rep_list(self):
        ind = self.database.get_current_rep_index()
        self.ui.filling.fill_tracker_tab(self.database.get_rep_names(), ind, self.database.get_current_rep_state())

