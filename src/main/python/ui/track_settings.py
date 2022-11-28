from typing import Optional

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from delegate import Delegate
from ui.source.track_settings import Ui_Dialog


class TrackSettings(Ui_Dialog):
    def __init__(self, parent: QMainWindow, tracked_list=None, ignored_list=None):
        if ignored_list is None:
            ignored_list = []
        if tracked_list is None:
            tracked_list = []
        self.dialog = QtWidgets.QDialog(parent)
        super().setupUi(self.dialog)
        self.sockets = {
            'add_to_ignored': Delegate(ignore_args=True),
            'add_to_tracked': Delegate(ignore_args=True),
            'remove_from_ignored': Delegate(ignore_args=True),
            'remove_from_tracked': Delegate(ignore_args=True),
        }
        self.__define_sockets()
        self.__ignored_list = ignored_list
        self.__tracked_list = tracked_list
        self.__fill_fields()

    def show(self):
        self.dialog.show()

    def __fill_fields(self):
        self.tracked_file_list.addItems(self.__tracked_list)
        self.ignore_file_list.addItems(self.__ignored_list)

    def __add_line_in_tracked(self, line: str):
        self.tracked_file_list.addItem(line)

    def __remove_line_from_tracked(self):
        self.tracked_file_list.takeItem(self.tracked_file_list.currentRow())

    def __remove_line_from_ignored(self):
        self.ignore_file_list.takeItem(self.ignore_file_list.currentRow())

    def __define_sockets(self):
        self.add_to_ignored.clicked.connect(self.sockets['add_to_ignored'])
        self.remove_from_tracked.clicked.connect(self.sockets['remove_from_tracked'])
        self.add_to_tracked.clicked.connect(self.sockets['add_to_tracked'])
        self.remove_from_ignored.clicked.connect(self.sockets['remove_from_ignored'])

        self.sockets['remove_from_tracked'].add(self.__remove_line_from_tracked)
        self.sockets['remove_from_ignored'].add(self.__remove_line_from_ignored)

        """
        теперь надо чтобы добавляла
        """
    #
    # def show(self):
    #     self.base_window.show()
    #
    # def __expand(self, *args, **kwargs):
    #     """
    #     Here i can extension my window, for example add widgets.
    #     """
    #
    #     # items = map(str, range(50))  # event list filling
    #     # for item in items:
    #     #     self.listWidget.addItem(QListWidgetItem(item))
    #
    # def request_dir_path(self) -> str:
    #     start_path = str(pathlib.Path.home())
    #     path = QFileDialog.getExistingDirectory(self.base_window, 'Directory for track', start_path)
    #     return path
    #
    # @validator.new_rep_name
    # def request_repository_name(self) -> Tuple[str, bool]:
    #     name, is_actual = QInputDialog.getText(self.base_window, 'Naming', 'Enter a name for the repository:')
    #     return name, is_actual
    #
    # def show_validator_except_mess(self, message: str):
    #     QMessageBox.warning(self.base_window, 'Validator except', message)
    #
    # def show_warning_mess(self, message: str, title: str = 'Warning!'):
    #     QMessageBox.warning(self.base_window, title, message)
    #
    # def text_user_request(self, message: str) -> Tuple[str, bool]:
    #     return QInputDialog.getText(self.base_window, 'Request', message)