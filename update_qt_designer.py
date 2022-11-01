"""
it's temporary file, delete its after develop
"""
import subprocess


class Console:
    def __init__(self):
        self._output = None
        self._input = None
        self._error = None

    def execute(self, command: str):
        pipe = subprocess.PIPE
        self.save_state(command, subprocess.Popen(command, stdout=pipe, stderr=pipe, encoding='utf-8'))
        # if not self._error:
        return [line.strip() for line in self._output]

    def save_state(self, command, answer):
        self._input = command
        if self.is_error(answer):
            self._error = True
            self._output = list(answer.stderr)
        else:
            self._error = False
            self._output = list(answer.stdout)

    @staticmethod
    def is_error(request):
        request.stderr = list(request.stderr)
        return bool(len(request.stderr))


def update_qt_file():
    source_path = r'C:\Users\ederm\Desktop\my_projects\repository\qt_designer_files\main_win.ui'
    qt_designer_path = r'C:\Users\ederm\Desktop\my_projects\repository\src\main\python\ui\qt_designer.py'
    command = ['pyuic5', '-x', source_path, '-o', qt_designer_path]
    console = Console()
    console.execute(command)
