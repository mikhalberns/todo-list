import os


class Config:
    @staticmethod
    def get_db_host() -> str:
        return os.environ.get('MONGO_HOST_NAME', 'host.docker.internal')

    @staticmethod
    def get_db_port() -> str:
        return os.environ.get('MONGO_PORT', '27018')

    @staticmethod
    def get_db_user() -> str:
        return os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')

    @staticmethod
    def get_db_user_pass() -> str:
        return os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'pass12345')


conf = Config()