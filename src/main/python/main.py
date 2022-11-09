import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app import Application
from qt_designer_files.window_update import update_qt_file  # temporary develop func

sys.path.append('src/main/python')

if __name__ == '__main__':
    update_qt_file()  # temporary develop func

    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext

    app = Application()
    app.start()

    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
