from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon


class QExtensionWindow(QMainWindow):
    def closeEvent(self, event):
        event.ignore()
        self.hide()