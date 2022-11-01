from .extension import Window
from .sockets import SocketsMixin

class Application(SocketsMixin, Window):
    pass