from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

from ui.app import Application


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    app = Application()
    # app.resize(250, 150)
    app.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)