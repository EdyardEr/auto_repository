from PyQt5.QtWidgets import QMainWindow


class QExtensionWindow(QMainWindow):
    def closeEvent(self, event):
        event.ignore()
        self.hide()