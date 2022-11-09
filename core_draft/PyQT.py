from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('имя окна')
        self.setGeometry(300, 300, 400, 400)  # расположение окна и размер

        self.empty_widget = QtWidgets.QLabel(self)  # пустой обьект
        self.is_widget_active = False

        # здесь добавляем элементы в окно вплоть до show
        main_text = QtWidgets.QLabel(self)  # передаём обьект
        main_text.setText('сам текст')
        main_text.move(100, 100)
        main_text.adjustSize()

        btn = QtWidgets.QPushButton(self)
        btn.move(70, 150)
        btn.setFixedWidth(200)
        btn.clicked.connect(self.button_event)  # привязывает кнопку
        btn.click()  # нажимает кнопку сам

    def button_event(self):
        print('pressed')
        if self.is_widget_active:
            text = ''
        else:
            text = 'появилась надпись'
        self.empty_widget.setText(text)
        self.is_widget_active = self.switch_bool(self.is_widget_active)

    @staticmethod
    def switch_bool(my_bool):
        return False if my_bool else True


if __name__ == '__main__':
    app = QApplication(sys.argv)  # передаём параметры системы
    window = Window()
    window.show()
    sys.exit(app.exec_())

