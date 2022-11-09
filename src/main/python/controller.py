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

    def fill_ui(self):
        self.ui.filling.fill_rep_list(self.get_repository_dirs().keys())
        self.ui.filling.fill_rep_path(self.get_repository_dirs()[self.ui.window.rep_list.currentText()])

    def get_repository_dirs(self) -> dict:
        return self.database['rep_dirs']

    def create_new_repository(self, *args, **kwargs):
        # print(args, kwargs)
        path = self.ui.window.request_dir_path()
        name = self.ui.window.request_repository_name()
        print(name)
        if type(name) == Exception:
            print('exception')
            self.valid_error(name)
        else:
            self.database['rep_dirs'][name] = path
            self.ui.filling.fill_rep_list(self.get_repository_dirs().keys())

    def valid_error(self, exception):
        self.ui.window.show_validator_except_mess(str(exception))
