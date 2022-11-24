from typing import Optional, Union

from database.application_data import AppData
from ui.ui import Ui
from .verifier import Verifier

class User:
    def __init__(self, ui: Ui, database: AppData, verifier: Verifier):
        self.ui = ui
        self.database = database
        self.verifier = verifier

    def write_rep_name(self) -> Optional[str]:
        new_name, is_actual = self.ui.window.request_repository_name()
        if not is_actual:
            return None
        elif type(new_name) == Exception:
            self.verifier.valid_error(new_name)
            return None
        elif self.verifier.is_name_exist(new_name):
            self.verifier.valid_error('This name is already used')
            return self.write_rep_name()
        else:
            return new_name

    def choose_rep_path(self) -> Optional[str]:
        new_path: str = self.ui.window.request_dir_path()
        if self.verifier.is_path_exist(new_path):
            self.verifier.valid_error('Repository in this directory already exist!')
            return None
        elif not new_path:
            return None
        else:
            return new_path

    def del_repository(self) -> Optional[str]:
        name = self.ui.window.rep_list.currentText()
        if not name:
            self.verifier.valid_error('Choose repository!')
            return None
        else:
            massage = f'WARNING!!!\nDo you want to delete "{name}" repository?\n(Yes/No)'
            correct_answers = ('Yes', 'yes')
            if self.text_conformation(massage, correct_answers):
                return name
        return None

    def text_conformation(self, massage: str, correct_answers: Union[list, tuple]) -> bool:
        answer, is_actual = self.ui.window.text_user_request(massage)
        if answer in correct_answers and is_actual:
            return True
        else:
            return False