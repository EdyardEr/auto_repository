from PyQt5.QtWidgets import QListWidgetItem

from .qt_designer_form import Ui_MainWindow


class AppWindow(Ui_MainWindow):
    def setupUi(self, *args, **kwargs):
        super().setupUi(*args, **kwargs)
        items = map(str, range(50))
        for item in items:
            self.listWidget.addItem(QListWidgetItem(item))
        # event = Event()
        # event.define_sockets()
