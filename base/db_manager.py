import psycopg2
from base.conf_parser import config

class DBManager:
    def __init__(self, database_name: str):
        self._database = database_name
        self._connection = None

    def connect(self):
        params = config()
        params['database'] = self._database
        self._connection = psycopg2.connect(**params)

    def close(self):
        if self._connection is not None:
            self._connection.close()

