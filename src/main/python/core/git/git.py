import os
import shutil
from functools import wraps

if __name__ == '__main__':
    from core.git.console import Console
    from core.git.gitignore import Gitignore
else:
    from .console import Console
    from .gitignore import Gitignore


def execute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self, command = func(*args, **kwargs)
        return self.cmd.execute(command)
    return wrapper


class Git:
    def __init__(self, work_dir_path: str = os.getcwd()):
        self.__work_dir_path = work_dir_path
        self.cmd = Console(self.__work_dir_path)
        self.gitignore = Gitignore(self.__work_dir_path)

    def delete_repository(self):
        result = False
        if self.gitignore.delete():
            result = True
        try:
            shutil.rmtree(self.__work_dir_path + r'\.git')
            result = True
        except FileNotFoundError:
            pass
        return result

    def is_valid(self) -> bool:
        successful, answer = self.status()
        return successful

    @execute
    def create_repository(self):
        self.gitignore.create()
        return self, 'git init'

    @execute
    def status(self):
        return self, 'git status'

    @execute
    def log(self):
        return 'git log --pretty=format:"%h - %cd : %s" --date=format:"%H:%M:%S %Y-%m-%d"'

    @execute
    def log_file(self, file_path):
        date_format = '--date=format:"%H:%M:%S %Y-%m-%d"'
        log_format = '--pretty=format:"%h - %cd : %s"'
        return f'git log --name-status {log_format} {date_format} -- {file_path}'

    @execute
    def add_all(self):
        return 'git add .'

    @execute
    def commit(self):
        return 'git commit -am "commit message"'

    @execute
    def checkout_file(self, file_path, commit_id):
        return f'git checkout {commit_id} {file_path}'

    @execute
    def log_name(self):
        return 'git log --name-only --pretty=format:""'

    @execute
    def test(self):
        return 'git commit -d'

    @execute
    def to_commite(self, commit_id):
        return f'git checkout {commit_id}'


if __name__ == '__main__':
    val = [True, ['On branch master', '', 'No commits yet', '', 'nothing to commit (create/copy files and use "git add" to track)']]
    inval = [False, ['fatal: not a git repository (or any of the parent directories): .git']]
    inval = [False, ['fatal: not a git repository (or any of the parent directories): .git']]
    path = r'C:\Users\ederm\Desktop\test_dir'
    git = Git(path)
    # print(git.delete_repository())
    # print(git.create_repository())
    print(git.status())
