import psycopg2
from base.conf_parser import config


def create_db_and_tabl(dbname: str) -> None:
    try:
        params = config()
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{dbname}'")
        if cur.fetchone():
            print(f"База {dbname} уже существует!")
            return
        cur.execute(f"CREATE DATABASE {dbname}")
        print(f"База с именем {dbname} создана!")
        cur.close()
        conn.close()

        params['dbname'] = dbname
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "CREATE TABLE employers (employer_id SERIAL PRIMARY KEY, name VARCHAR(300) NOT NULL, url VARCHAR(300) NOT NULL);")
        cur.execute(
            "CREATE TABLE vacancies (vacancy_id SERIAL PRIMARY KEY, employer_id INTEGER REFERENCES employers(employer_id), name VARCHAR NOT NULL, description TEXT, area VARCHAR(100) NOT NULL, url VARCHAR(300), salary_from INTEGER, salary_to INTEGER, currency VARCHAR(30), published_at TIMESTAMP NOT NULL);")

        conn.commit()
        cur.close()
        conn.close()
        print("Таблицы employers и vacancies созданы!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")


create_db_and_tabl("my_database")