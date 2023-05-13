import psycopg2
from src.hh_api_key import HHApi
from base.config import user, password


def insert_data(dbname: str, search_query) -> None:
    conn = psycopg2.connect(database=dbname, user=user, password=password, host="localhost", port="5432")
    cur = conn.cursor()
    hh_api = HHApi()
    employers_data, vacancies_data = hh_api.get_vacancies(search_query)
    for emp in employers_data:
        cur.execute("INSERT INTO employers (employers_id, name, url) VALUES (%s, %s, %s)",
                    (emp['employer_id'], emp['name'], emp['url']))
    for vac in vacancies_data:
        cur.execute(
            "INSERT INTO vacancies"
            "(employer_id, name, description, area, url, salary_from, salary_to, currency, published_at)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", vac['employer_id'], vac['vacancy_name'],
            vac['description'], vac['area'], vac['url'], vac['salary_from'], vac['salary_to'], vac['currency'],
            vac['published_at'])

        conn.commit()
        cur.close()
        conn.close()
