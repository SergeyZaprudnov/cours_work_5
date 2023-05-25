import psycopg2
from src.hh_api_key import HHApi
from base.config import user, password


def insert_data(dbname: str, search_query) -> None:
    conn = psycopg2.connect(database=dbname, user=user, password=password, host="localhost", port="5432")
    cur = conn.cursor()
    hh_api = HHApi()
    employers_data, vacancies_data = hh_api.get_vacancies(search_query)

    for employer in employers_data:
        cur.execute("INSERT INTO employers (employer_id, name, url) VALUES (%s, %s, %s)",
                    (employer['employer_id'], employer['name'], employer['url']))
    for vacancy in vacancies_data:
        cur.execute(
            "INSERT INTO vacancies "
            "(employer_id, name, description, area, url, salary_from, salary_to, currency, published_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (vacancy['employer_id'], vacancy['vacancy_name'], vacancy['description'], vacancy['area'], vacancy['url'],
             vacancy['salary_from'], vacancy['salary_to'], vacancy['currency'], vacancy['published_at']))

    conn.commit()
    cur.close()
    conn.close()
