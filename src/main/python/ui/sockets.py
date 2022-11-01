from .extension import Window
from core import controller

class SocketsMixin:
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        # print('socket')
        super().__init__(*args, **kwargs)
        self.__link()

    def __link(self: 'Window'):
        """
        here we link widgets and controller func
        """
        self.create_rep.clicked.connect(controller.test_controller_func)
        self.del_rep.clicked.connect(controller.test_controller_func)
        self.track.clicked.connect(controller.test_controller_func)


