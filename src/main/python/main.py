"""
it's utility update qt file, delete its after develop
"""

from update_qt_designer import update_qt_file as update
update()
"""
"""
import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app import Application


sys.path.append('src/main/python')

if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext

    app = Application()
    app.start()

    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
