from .track_settings import TrackSettings
from .window import Window
from delegate import Delegate

class Sockets:
    def __init__(self, window: Window):
    # def __init__(self, window: Window, track_settings: TrackSettings):
        """
            here we link widgets and events
        """
        self.create_rep_button = Delegate(ignore_args=True)
        window.create_rep.clicked.connect(self.create_rep_button)

        self.del_rep_button = Delegate(ignore_args=True)
        window.del_rep.clicked.connect(self.del_rep_button)

        self.track_settings_button = Delegate(ignore_args=True)
        window.track_settings.clicked.connect(self.track_settings_button)

        self.track_dir_button = Delegate(ignore_args=True)
        window.track_dir.clicked.connect(self.track_dir_button)

        self.change_rep_combo_box = Delegate()
        window.rep_list.currentIndexChanged.connect(self.change_rep_combo_box)

        # self.add_to_ignored_button = Delegate()
        # track_settings.add_to_ignored.clicked.connect(self.add_to_ignored_button)
        #
        # self.remove_from_tracked_button = Delegate()
        # track_settings.remove_from_tracked.clicked.connect(self.remove_from_tracked_button)
        #
        # self.add_to_tracked_button = Delegate()
        # track_settings.add_to_tracked.clicked.connect(self.add_to_tracked_button)
        #
        # self.remove_from_ignored_button = Delegate()
        # track_settings.remove_from_ignored.clicked.connect(self.remove_from_ignored_button)







