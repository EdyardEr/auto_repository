from .ui_extension import AppWindow


def event_func():
    print('click')

class Event:
    def define_sockets(self: 'AppWindow'):
        self.create_rep.clicked(event_func)

