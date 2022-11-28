import os
import subprocess
from typing import List, Union, Tuple

class Console:
    def __init__(self, path: str = os.getcwd()):
        self.__output = None
        self.__input = None
        self.__successful = None
        self.__path = path

    def execute(self, command: Union[str, List[str], Tuple[str]]) -> list:
        pipe = subprocess.PIPE
        try:
            answer = subprocess.Popen(command, stdout=pipe, stderr=pipe, encoding='utf-8', cwd=self.__path)
            self.__save_state(command, answer)
            return [self.__successful, [line.strip() for line in self.__output]]
        except NotADirectoryError:
            return [False, ['directory for git incorrect!']]

    def __save_state(self, command, answer: subprocess.Popen):
        self.__input = command
        if self.__is_error(answer):
            self.__successful = False
            self.__output = list(answer.stderr)
        else:
            self.__successful = True
            self.__output = list(answer.stdout)

    @staticmethod
    def __is_error(request) -> bool:
        request.stderr = list(request.stderr)
        return bool(len(request.stderr))


if __name__ == '__main__':
    path = r'C:\Users\ederm\Desktop\my_projects\documentation'
    command = r'git status'
    cmd = Console(path)
    print(cmd.execute(command))