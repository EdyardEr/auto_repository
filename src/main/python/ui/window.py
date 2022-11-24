import pathlib
from typing import Tuple

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog

from .q_extension_window import QExtensionWindow
from .window_source import Ui_MainWindow
from ui.validators import validator


class Window(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.base_window = QExtensionWindow()

        super().setupUi(self.base_window)
        self.__expand(*args, **kwargs)

    def show(self):
        self.base_window.show()

    def __expand(self, *args, **kwargs):
        """
        Here i can extension my window, for example add widgets.
        """

        # items = map(str, range(50))  # event list filling
        # for item in items:
        #     self.listWidget.addItem(QListWidgetItem(item))

    def request_dir_path(self) -> str:
        start_path = str(pathlib.Path.home())
        path = QFileDialog.getExistingDirectory(self.base_window, 'Directory for track', start_path)
        return path

    @validator.new_rep_name
    def request_repository_name(self) -> Tuple[str, bool]:
        name, is_actual = QInputDialog.getText(self.base_window, 'Naming', 'Enter a name for the repository:')
        return name, is_actual

    def show_validator_except_mess(self, message: str):
        QMessageBox.warning(self.base_window, 'Validator except', message)

    def show_warning_mess(self, message: str, title: str = 'Warning!'):
        QMessageBox.warning(self.base_window, title, message)

    def text_user_request(self, message: str) -> Tuple[str, bool]:
        return QInputDialog.getText(self.base_window, 'Request', message)

