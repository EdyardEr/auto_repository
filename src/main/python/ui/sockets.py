from .extension import Window
from controller import Controller


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
        self.create_rep.clicked.connect(Controller.create_new_repository())
        self.del_rep.clicked.connect(Controller.test_controller_func)
        self.track.clicked.connect(Controller.test_controller_func)


