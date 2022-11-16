from typing import Dict

from .window import Window
from .delegate import Delegate

class Sockets:
    def __init__(self, window: Window):
        """
            here we link widgets and events
        """
        self.create_rep_button = Delegate()
        window.create_rep.clicked.connect(self.create_rep_button)

        self.del_rep_button = Delegate()
        window.del_rep.clicked.connect(self.del_rep_button)

        self.track_dir = Delegate()
        window.track_dir.clicked.connect(self.track_dir)

        self.change_rep_combo_box = Delegate()
        window.rep_list.currentIndexChanged.connect(self.change_rep_combo_box)





