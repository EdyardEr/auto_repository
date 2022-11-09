from database.db import AppData
from controller import Controller
from ui.ui import Ui

class Application:
    def __init__(self):
        self._database = AppData()
        self._ui = Ui()
        self._controller = Controller(self._ui, self._database)

    def start(self):
        self._ui.show()

