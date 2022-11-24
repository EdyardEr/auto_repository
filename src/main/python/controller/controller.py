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
        self.watchers = WatcherManager(self.database, self.ui)
        self.connect_ui()

    def connect_ui(self):
        self.__create_ui_links()
        self.__fill_ui()

    def __create_ui_links(self):
        self.ui.sockets.create_rep_button.add(self.create_new_repository)
        self.ui.sockets.del_rep_button.add(self.del_repository)
        self.ui.sockets.change_rep_combo_box.add(self.switch_combo_box)
        self.ui.sockets.track_dir.add(self.track_rep)

    def __fill_ui(self):
        current_index = self.database.get_current_rep_index()
        self.ui.filling.fill_rep_list(self.database.get_rep_names())
        # self.update_ui_tracker_tab()
        self.ui.filling.choose_rep(current_index)

    def track_rep(self):
        current_name = self.database.get_current_rep_name()
        if self.database.get_current_rep_track_state():
            self.watchers.turn_off_watcher(current_name)
        else:
            self.watchers.turn_on_watcher(current_name)

    def switch_combo_box(self, line_ind):
        self.database.set_current_rep_index(line_ind)
        if line_ind != -1:
            self.update_ui_tracker_tab()
        else:
            self.clear_ui_tracker_tab()

    def create_new_repository(self):
        new_path = self.user.choose_rep_path()
        if new_path is None:
            return
        new_name = self.user.write_rep_name()
        if new_name is None:
            return
        self.database.set_new_rep(new_name, new_path, False)
        self.watchers.add_new_watcher(new_name, new_path)
        self.ui.filling.add_repository(new_name)
        self.ui.filling.choose_rep(self.database.get_reps_count() - 1)

    def del_repository(self):
        name = self.user.del_repository()
        if name is None:
            return
        self.database.del_rep(name)
        self.ui.filling.reset_rep_list(self.database.get_rep_names())

    def update_ui_tracker_tab(self):
        self.ui.filling.fill_events_list(self.watchers.get_current_events_list())
        self.ui.filling.fill_rep_path(self.database.get_current_rep_path())
        self.ui.filling.switch_track_indicator(self.database.get_current_rep_track_state())

    def clear_ui_tracker_tab(self):
        self.ui.filling.clear_events_list()
        self.ui.filling.fill_rep_path('')
        self.ui.filling.switch_track_indicator(False)
