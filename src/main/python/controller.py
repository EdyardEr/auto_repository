from database.db import AppData
from ui.extension import
app_data = AppData()

class Controller:
    @classmethod
    def test_controller_func(cls):
        print('click')

    @classmethod
    def get_repository_dirs(cls) -> dict:
        return app_data['rep_dirs']

    @classmethod
    def create_new_repository(cls):
        pass
