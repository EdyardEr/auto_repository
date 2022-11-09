import subprocess
import copy

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

    # def to_commite(self, commit_id):
    #     print(self.cmd.execute(f'git checkout {commit_id}'))


if __name__ == '__main__':
    git = Git()
    # git.status()