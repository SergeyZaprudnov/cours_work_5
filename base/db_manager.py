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

    def get_companies_and_vacancies_count(self):
        self.connect()
        cur = self._connection.cursor()
        cur.execute("SELECT e.name AS company_name, COUNT(v.vacancy_id) AS vacancies_count"
                    "FROM employers e LEFT JOIN vacancies v ON e.employer_id = v.employer_id"
                    "GROUP BY e.name"
                    "ORDER BY vacancies_count DESC;")
        rows = cur.fetchall()
        for r in rows:
            print(f"{r}: {r} vacancies")
        cur.close()
        self.close()
