import psycopg2
from base.config import user, password


class DBManager:
    def __init__(self, database_name: str):
        self._database = database_name

    def get_companies_and_vacancies_count(self):

        conn = psycopg2.connect(host="localhost", database=self._database, user=user, password=password)
        cur = conn.cursor()
        cur.execute(
            "SELECT e.name AS company_name, COUNT(v.vacancy_id) AS vacancies_count "
            "FROM employers e LEFT JOIN vacancies v ON e.employer_id = v.employer_id "
            "GROUP BY e.name "
            "ORDER BY vacancies_count DESC;"
        )
        rows = cur.fetchall()
        for r in rows:
            print(f"{r}: {r} vacancies")
        cur.close()
        conn.close()

    def get_all_vacancies(self):
        conn = psycopg2.connect(host="localhost", database=self._database, user=user, password=password)
        cur = conn.cursor()
        cur.execute('''
                SELECT e.name AS company_name, v.name AS vacancy_name, v.salary_from, v.salary_to, v.currency, v.url
                FROM employers e
                JOIN vacancies v ON e.employer_id = v.employer_id;
                ''')
        rows = cur.fetchall()
        for r in rows:
            print(r)
        cur.close()
        conn.close()

    def get_avg_salary(self):
        conn = psycopg2.connect(host="localhost", database=self._database, user=user, password=password)
        cur = conn.cursor()
        cur.execute("SELECT AVG((salary_from + salary_to) / 2) as average_salary FROM vacancies;")
        rows = cur.fetchall()
        print(f"Средняя заработная плата от: {rows}")
        cur.close()
        conn.close()

    def get_vacancies_with_higher_salary(self):
        conn = psycopg2.connect(host="localhost", database=self._database, user=user, password=password)
        cur = conn.cursor()
        cur.execute("SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)")
        rows = cur.fetchall()
        for r in rows:
            print(f"id: {r[0]} Вакансия: {r[2], r[3], r[4], r[5], r[6]}")
        cur.close()
        conn.close()

    def get_vacancies_with_keyword(self, keyword):
        conn = psycopg2.connect(host="localhost", database=self._database, user=user, password=password)
        cur = conn.cursor()
        sql_query = "SELECT * FROM vacancies WHERE name LIKE %s"
        search_params = (f'%{keyword}%',)
        cur.execute(sql_query, search_params)
        result = cur.fetchall()
        for r in result:
            print(f"id: {r[0]} Вакансия: {r[2], r[3], r[4], r[5], r[6]}")
        cur.close()
        conn.close()
