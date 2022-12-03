import os
import shutil
import stat
from functools import wraps

if __name__ == '__main__':
    from core.git.console import Console
    from core.git.gitignore import Gitignore
else:
    from .console import Console


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
        # self.gitignore = Gitignore(self.__work_dir_path)

    @staticmethod
    def del_readonly(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    def delete_repository(self):
        try:
            shutil.rmtree(self.__work_dir_path + r'\.git', onerror=self.del_readonly)
            return True
        except FileNotFoundError:
            return False

    def is_valid(self) -> bool:
        successful, answer = self.status()
        return successful

    @execute
    def create_repository(self):
        return self, 'git init'

    @execute
    def remove_from_index(self):
        return self, 'git rm --cached *'

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
        return self, 'git add .'

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
    # val = [True, ['On branch master', '', 'No commits yet', '', 'nothing to commit (create/copy files and use "git add" to track)']]
    # inval = [False, ['fatal: not a git repository (or any of the parent directories): .git']]
    # inval = [False, ['fatal: not a git repository (or any of the parent directories): .git']]
    path = r'C:\Users\ederm\Desktop\test_dir'
    git = Git(path)
    # print(git.delete_repository())
    # print(git.create_repository())
    # print(git.add_all())
    # print(git.status())
    # print(git.remove_from_index())
    print(git.delete_repository())

