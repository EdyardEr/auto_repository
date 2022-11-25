import subprocess
from typing import List, Union, Tuple

class Console:
    def __init__(self):
        self.__output = None
        self.__input = None
        self.__error = None

    def execute(self, command: Union[str, List[str], Tuple[str]]) -> List[bool, list]:
        pipe = subprocess.PIPE
        self.__save_state(command, subprocess.Popen(command, stdout=pipe, stderr=pipe, encoding='utf-8'))
        return [self.__error, [line.strip() for line in self.__output]]

    def __save_state(self, command, answer: subprocess.Popen):
        self.__input = command
        if self.__is_error(answer):
            self.__error = True
            self.__output = list(answer.stderr)
        else:
            self.__error = False
            self.__output = list(answer.stdout)

    @staticmethod
    def __is_error(request) -> bool:
        request.stderr = list(request.stderr)
        return bool(len(request.stderr))
