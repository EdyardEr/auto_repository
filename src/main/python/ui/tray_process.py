from typing import Dict

from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMenu, QAction, qApp, QMainWindow

from .delegate import Delegate

class TrayProcess:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.sockets: Dict[str, Delegate] = {'show_action': Delegate()}
        self._define_icon()
        self._create_menu()

    def _define_icon(self):
        self.tray_icon = QSystemTrayIcon(self.window)
        self.tray_icon.setIcon(self.window.style().standardIcon(QStyle.SP_ComputerIcon))

    def _create_menu(self):
        menu_points = {'show_action': QAction("Show", self.window),
                       'hide_action': QAction("Hide", self.window),
                       'quit_action': QAction("Exit", self.window)}

        tray_menu = QMenu()
        for action in menu_points.values():
            tray_menu.addAction(action)

        self.tray_icon.setContextMenu(tray_menu)
        self._add_menu_sockets(menu_points)
        self._connect_to_sockets()
        # show_action.triggered.connect(self.window.show)
        # hide_action.triggered.connect(self.window.hide)
        # quit_action.triggered.connect(qApp.quit)

    def _add_menu_sockets(self, menu_points: Dict[str, QAction]):
        for name, point in menu_points.items():
            delegate = Delegate(ignore_args_args=True)
            point.triggered.connect(delegate)
            self.sockets[name] = delegate

    def _connect_to_sockets(self):
        self.sockets['show_action'].add(self.window.show)
        self.sockets['hide_action'].add(self.window.hide)
        self.sockets['quit_action'].add(qApp.quit)

    def show(self):
        self.tray_icon.show()

