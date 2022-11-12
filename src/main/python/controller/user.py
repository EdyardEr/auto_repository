from typing import Optional

from ui.ui import Ui
from .verifier import Verifier

class User:
    def __init__(self, ui: Ui, verifier: Verifier):
        self.ui = ui
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