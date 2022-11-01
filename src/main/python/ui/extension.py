from PyQt5.QtWidgets import QListWidgetItem, QMainWindow

from .qt_designer import Ui_MainWindow


class Window(Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # print('extension')
        self._base_window = QMainWindow()
        super().setupUi(self._base_window)
        self.__expand(*args, **kwargs)

    def show(self):
        self._base_window.show()

    def __expand(self, *args, **kwargs):
        """
        Here i can extension my window, for example add widgets.
        """
        # items = map(str, range(50))
        # for item in items:
        #     self.listWidget.addItem(QListWidgetItem(item))
