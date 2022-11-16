from .window import Window
from .filling import Filling
from .sockets import Sockets
from .tray_process import TrayProcess

class Ui:
    def __init__(self):
        self.window = Window()
        self.tray_process = TrayProcess(self.window.base_window)
        self.sockets = Sockets(self.window)
        self.filling = Filling(self.window)

    def show(self):
        self.window.show()
        self.tray_process.show()
