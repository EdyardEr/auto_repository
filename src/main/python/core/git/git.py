if __name__ == '__main__':
    from core.git.console import Console
else:
    from .console import Console


class Git:
    def __init__(self):
        self.cmd = Console()

    def status(self):
        print(self.cmd.execute('git status'))

    def log(self):
        print(self.cmd.execute('git log --pretty=format:"%h - %cd : %s" --date=format:"%H:%M:%S %Y-%m-%d"'))

    def log_file(self, file_path):
        date_format = '--date=format:"%H:%M:%S %Y-%m-%d"'
        log_format = '--pretty=format:"%h - %cd : %s"'
        print(self.cmd.execute(f'git log --name-status {log_format} {date_format} -- {file_path}'))

    def add_all(self):
        print(self.cmd.execute('git add .'))

    def commit(self):
        print(self.cmd.execute('git commit -am "commit message"'))

    def checkout_file(self, file_path, commit_id):
        print(self.cmd.execute(f'git checkout {commit_id} {file_path}'))

    def log_name(self):
        print(self.cmd.execute('git log --name-only --pretty=format:""'))

    def test(self):
        print(self.cmd.execute('git commit -d'))
    # def to_commite(self, commit_id):
    #     print(self.cmd.execute(f'git checkout {commit_id}'))


if __name__ == '__main__':
    git = Git()
    # git.status()
    git.test()
