from core.git.console import Console

def update_qt_file():
    """
    it's utility update source_window.py from qt designer file
    """
    source_dir_path = r'C:\Users\ederm\Desktop\my_projects\repository\qt_designer_files\\'
    destination_dir = r'C:\Users\ederm\Desktop\my_projects\repository\src\main\python\ui\source\\'
    names = [['main_win.ui', 'window.py'], ['track_settings.ui', 'track_settings.py']]

    console = Console()
    for source_file_name, destination_name in names:
        source_path = source_dir_path + source_file_name
        destination_path = destination_dir + destination_name
        console.execute(['pyuic5', '-x', source_path, '-o', destination_path])


if __name__ == '__main__':
    update_qt_file()