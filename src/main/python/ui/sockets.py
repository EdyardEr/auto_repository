from .extension import Window

def test_controller_func():
    print('click')


class SocketsMixin:
    def __init__(self, *args, **kwargs):
        # print('socket')
        super().__init__(*args, **kwargs)
        self.__link()

    def __link(self: 'Window'):
        """
        here we link widgets and controller func
        """
        self.create_rep.clicked.connect(test_controller_func)


