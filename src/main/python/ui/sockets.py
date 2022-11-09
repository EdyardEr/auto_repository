from .extension import Window
from event import Event

class Sockets:
    def __init__(self, window: Window):
        """
            here we link widgets and events
        """
        self.create_rep_button = Event()
        window.create_rep.clicked.connect(self.create_rep_button)




