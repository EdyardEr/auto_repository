from typing import Tuple, Optional

from PyQt5.QtWidgets import QInputDialog, QDialog, QListWidget, QWidget

from delegate import Delegate
from ui.source.track_settings import Ui_Dialog
from ui.validators import validator


class TrackSettings(QDialog):
    def __init__(self, parent: QWidget, settings: Optional[dict] = None):
        super().__init__(parent)
        self.basis = Ui_Dialog()
        self.basis.setupUi(self)

        if settings is not None:
            self.basis.tracked_file_list.addItems(settings['tracked'])
            self.basis.ignore_file_list.addItems(settings['ignored'])

        self.sockets = {
            'add_to_ignored': Delegate(ignore_args=True),
            'add_to_tracked': Delegate(ignore_args=True),
            'remove_from_ignored': Delegate(ignore_args=True),
            'remove_from_tracked': Delegate(ignore_args=True),
        }
        self.__define_sockets()
        self.__connect_internal_sockets()

    def result(self) -> dict:
        settings = {
            'ignored': self.__get_items_form_list(self.basis.ignore_file_list),
            'tracked': self.__get_items_form_list(self.basis.tracked_file_list),
        }
        return settings

    @staticmethod
    def __get_items_form_list(list_widget: QListWidget):
        items = []
        for index in range(list_widget.count()):
            items.append(list_widget.item(index).text())
        return items

    def __add_line_in_tracked(self, line: str):
        self.basis.tracked_file_list.addItem(line)

    def __add_line_in_ignored(self, line: str):
        self.basis.ignore_file_list.addItem(line)

    def __remove_line_from_tracked(self):
        self.basis.tracked_file_list.takeItem(self.basis.tracked_file_list.currentRow())

    def __remove_line_from_ignored(self):
        self.basis.ignore_file_list.takeItem(self.basis.ignore_file_list.currentRow())

    def __add_line_to_tracked(self):
        line, is_actual = self.__request_line()
        if is_actual:
            self.__add_line_in_tracked(line)

    def __add_line_to_ignored(self):
        line, is_actual = self.__request_line()
        if is_actual:
            self.__add_line_in_ignored(line)

    # @validator.new_rep_name ## добавить валидацию! или нет)
    def __request_line(self) -> Tuple[str, bool]:
        text = 'Enter name, inner path or extension:'
        line, is_actual = QInputDialog.getText(self, 'New line', text)
        return line, is_actual

    def __define_sockets(self):
        self.basis.add_to_ignored.clicked.connect(self.sockets['add_to_ignored'])
        self.basis.remove_from_tracked.clicked.connect(self.sockets['remove_from_tracked'])
        self.basis.add_to_tracked.clicked.connect(self.sockets['add_to_tracked'])
        self.basis.remove_from_ignored.clicked.connect(self.sockets['remove_from_ignored'])

    def __connect_internal_sockets(self):
        self.sockets['remove_from_tracked'].add(self.__remove_line_from_tracked)
        self.sockets['remove_from_ignored'].add(self.__remove_line_from_ignored)
        self.sockets['add_to_tracked'].add(self.__add_line_to_tracked)
        self.sockets['add_to_ignored'].add(self.__add_line_to_ignored)

    # def show_validator_except_mess(self, message: str):
    #     QMessageBox.warning(self.base_window, 'Validator except', message)