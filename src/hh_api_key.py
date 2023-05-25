# Класс для получения данных с ресурса HeadHunter
import requests


class HHApi:
    def __init__(self):
        self.employer_data = None
        self.url_hh = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        params = {'text': search_query, 'per_page': 100, 'area': 113}
        vacancies_data = []
        response = requests.get(self.url_hh, params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                if vacancy['employer']['name'] == search_query:
                    if vacancy['salary'] is not None:
                        vacancy_data = {
                            'id_vacancy': vacancy['id'],
                            'employer_id': vacancy['employer']['id'],
                            'vacancy_name': vacancy['name'],
                            'description': vacancy['snippet']['responsibility'],
                            'area': vacancy['area']['name'],
                            'url': vacancy['alternate_url'],
                            'salary_from': vacancy['salary']['from'],
                            'salary_to': vacancy['salary']['to'],
                            'currency': vacancy['salary']['currency'],
                            'published_at': vacancy['published_at']
                        }
                        vacancies_data.append(vacancy_data)
                        self.employer_data = HHApi.get_employers(vacancy_data['employer_id'])
                    else:
                        continue
        else:
            print("Error:", response.status_code)
        return self.employer_data, vacancies_data

    @staticmethod
    def get_employers(employer_id):
        employers = []
        response_employers = requests.get(f'https://api.hh.ru/employers/{employer_id}')
        if response_employers.ok:
            data_employer = response_employers.json()
            employer = {'employer_id': data_employer['id'], 'name': data_employer['name'],
                        'url': data_employer['site_url']}
            employers.append(employer)
        return employers
