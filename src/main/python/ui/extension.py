import pathlib
from typing import Tuple

from PyQt5.QtWidgets import QListWidgetItem, QMainWindow, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtCore import QCoreApplication, QUrl

from event import Event
from .source_window import Ui_MainWindow
from ui.validators import validator


class Window(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self._base_window = QMainWindow()
        super().setupUi(self._base_window)
        self.__expand(*args, **kwargs)

    def show(self):
        self._base_window.show()

    def __expand(self, *args, **kwargs):
        """
        Here i can extension my window, for example add widgets.
        """

        # items = map(str, range(50))  # event list filling
        # for item in items:
        #     self.listWidget.addItem(QListWidgetItem(item))

    def request_dir_path(self) -> str:
        start_path = str(pathlib.Path.home())
        path = QFileDialog.getExistingDirectory(self._base_window, 'Directory for track', start_path)
        return path

    @validator.new_rep_name
    def request_repository_name(self) -> str:
        name, is_act = QInputDialog.getText(self._base_window, 'Naming', 'Enter a name for the repository:')
        return name

    def show_validator_except_mess(self, message):  # test with mess widgets
        QMessageBox.warning(self._base_window, 'Validator except', message)

