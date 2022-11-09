from git import Git

if __name__ == '__main__':
    """c02fd2d dacd81a c99285e"""
    name = r'C:\Users\ederm\Desktop\my_projects\repository\watch_dir\dir\file3.py'
    state = ['99c77be - 18:43:02 2022-10-25 : com file3"', 'M\tdir/file3.py', '', 'd26b6ec - 13:29:57 2022-10-25 : 3mod 2cre 1del', 'A\tdir/file3.py']
    commit_id = 'c99285e'
    git = Git()
    git.log_file(name)
    # git.log_name()
    # git.checkout_file(name, commit_id)