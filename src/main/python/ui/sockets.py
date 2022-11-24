from .window import Window
from delegate import Delegate

class Sockets:
    def __init__(self, window: Window):
        """
            here we link widgets and events
        """
        self.create_rep_button = Delegate(ignore_args=True)
        window.create_rep.clicked.connect(self.create_rep_button)

        self.del_rep_button = Delegate(ignore_args=True)
        window.del_rep.clicked.connect(self.del_rep_button)

        self.track_dir = Delegate(ignore_args=True)
        window.track_dir.clicked.connect(self.track_dir)

        self.change_rep_combo_box = Delegate()
        window.rep_list.currentIndexChanged.connect(self.change_rep_combo_box)





