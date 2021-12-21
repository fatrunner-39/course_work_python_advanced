import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


GROUPS_TOKEN = os.environ.get("GROUPS_TOKEN")
USERS_TOKEN = os.environ.get("USERS_TOKEN")

class DBSettings:
    def __init__(self):
        self.HOST = os.environ.get("HOST")
        self.PORT = os.environ.get("PORT")
        self.NAME = os.environ.get("NAME")
        self.USER_ = os.environ.get("USER_")
        self.PASSWORD = os.environ.get("PASSWORD")

    def create_db(self):
        return (
            f'postgresql+psycopg2://'
            f'{self.USER_}:{self.PASSWORD}'
            f'@{self.HOST}:{self.PORT}'
            f'/{self.NAME}'
        )

db_settings = DBSettings()


if __name__ == '__main__':
    print(db_settings.create_db())
    print(USERS_TOKEN)
    print(GROUPS_TOKEN)
