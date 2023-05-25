CREATE TABLE employers (
    employer_id SERIAL PRIMARY KEY,
    name VARCHAR(300) NOT NULL,
    url VARCHAR(300) NOT NULL
);

CREATE TABLE vacancies (
    vacancy_id SERIAL PRIMARY KEY,
    employer_id INTEGER REFERENCES employers(employer_id),
    name VARCHAR NOT NULL,
    description TEXT,
    area VARCHAR(60) NOT NULL,
    url VARCHAR(300) NOT NULL,
    salary_from INTEGER,
    salary_to INTEGER,
    currency VARCHAR(20),
    published_at TIMESTAMP NOT NULL
);

SELECT * FROM employers;
SELECT * FROM vacancies;

INSERT INTO employers (employer_id, name, url) VALUES (%s, %s, %s);
INSERT INTO vacancies (employer_id, name, description, area, url, salary_from, salary_to, currency, published_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

SELECT e.name AS company_name, COUNT(v.vacancy_id) AS vacancies_count
FROM employers e LEFT JOIN vacancies v ON e.employer_id = v.employer_id
GROUP BY e.name
ORDER BY vacancies_count DESC;

SELECT e.name AS company_name, v.name AS vacancy_name, v.salary_from, v.salary_to, v.currency, v.url
FROM employers e
JOIN vacancies v ON e.employer_id = v.employer_id;

SELECT AVG((salary_from + salary_to) / 2) as average_salary FROM vacancies;

SELECT AVG((salary_from + salary_to) / 2) as average_salary FROM vacancies;

SELECT * FROM vacancies WHERE name LIKE %s;