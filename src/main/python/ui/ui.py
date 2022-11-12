from .window import Window
from .filling import Filling
from .sockets import Sockets
# from .validator import Validator

class Ui:
    def __init__(self):
        self.window = Window()
        self.sockets = Sockets(self.window)
        self.filling = Filling(self.window)

    def show(self):
        self.window.show()
