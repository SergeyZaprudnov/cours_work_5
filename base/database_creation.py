import psycopg2
from base.config import user, password


def create_db_and_tabl(dbname: str) -> None:
    try:
        conn = psycopg2.connect(database="postgres", user=user, password=password, host="localhost", port="5432")
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{dbname}'")
        if cur.fetchone():
            print(f"База данных {dbname} уже существует.")
            return

        cur.execute(f"CREATE DATABASE {dbname}")
        print(f"База данных {dbname} успешно создана.")
        cur.close()
        conn.close()

        conn = psycopg2.connect(database=dbname, user=user, password=password, host="localhost", port="5432")
        cur = conn.cursor()

        cur.execute("""
                    CREATE TABLE employers (
                           employer_id SERIAL PRIMARY KEY,
                           name VARCHAR(255) NOT NULL,
                           url VARCHAR(255) NOT NULL
                        );""")
        cur.execute("""
                    CREATE TABLE vacancies (
                            vacancy_id SERIAL PRIMARY KEY,
                            employer_id INTEGER REFERENCES employers(employer_id),
                            name VARCHAR NOT NULL,
                            description TEXT,
                            area VARCHAR(50) NOT NULL,
                            url VARCHAR(255),
                            salary_from INTEGER,
                            salary_to INTEGER,
                            currency VARCHAR(10),
                            published_at TIMESTAMP NOT NULL
                        );""")

        conn.commit()
        cur.close()
        conn.close()
        print("Таблицы employers и vacancies успешно созданы.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
