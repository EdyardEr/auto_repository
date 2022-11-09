import pathlib
from typing import Tuple

from PyQt5.QtWidgets import QListWidgetItem, QMainWindow, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtCore import QCoreApplication, QUrl

from event import Event
from .qt_designer import Ui_MainWindow

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

        # self.fill_rep_list()

    # def fill_rep_list(self):
    #     _translate = QCoreApplication.translate
    #     # rep_names = self.controller.get_repository_dirs().keys()
    #     rep_names = ['one', 'two']
    #     self.rep_list.addItems(rep_names)

        # items = map(str, range(50))  # event list filling
        # for item in items:
        #     self.listWidget.addItem(QListWidgetItem(item))

    def request_repository_name(self) -> str:
        name, is_act = QInputDialog.getText(self._base_window, 'Repository name', 'Enter a name for the repository:')
        return name

    def register_new_repository(self) -> Tuple[str, str]:
        return self.request_dir_path(), self.request_repository_name()

    def request_dir_path(self) -> str:
        start_path = str(pathlib.Path.home())
        path = QFileDialog.getExistingDirectory(self._base_window, 'Directory for track', start_path)
        print(path)
        return path

    def run_msg(self):  # test with mess widgets
        pass
        # print(QMessageBox.information(self._base_window, 'dfldkjf', 'uignyitn'))
        # mess_win = QMessageBox(self._base_window)
        # mess_win.setText('your message text')
        # mess_win.setDetailedText('detail about your issue')
        # mess_win.setWindowTitle('Full Drive')
        # mess_win.setIcon(QMessageBox.Information)
        # mess_win.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # mess_win.exec_()
