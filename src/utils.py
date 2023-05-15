from base.database_creation import create_db_and_tabl
from base.insert_db import insert_data
from base.db_manager import DBManager


def start_of_the_program():
    print("Добро пожаловать в программу по работе с базой данных PostgreSQL\n"
          "Программа позволяет получить сведения о работодателях, а так же, их вакансиях с ресурса HeadHunter.\n"
          "Полученные Вами данные будут сохраняться в базу данных.\n"
          "Приятного Вам пользования!")

    while True:
        print("Если Вы хотите создать базу данных, введите цифру  1\n"
              "Если Вы хотите завершить работу с программой, введите цифру 2")
        choice = input("Ведите номер выбранного Вами варианта: ")
        if choice == '1':
            return 1
        elif choice == '2':
            print("Всего Вам хорошего. Благодарим за использование данной программы.")
            break
        else:
            print("Вы сделали не правильный выбор, попробуйте еще раз.\n")


def creating_a_user_database():
    if start_of_the_program() == 1:
        database_name = input("Введите название Вашей базы данных: ").lower()
        create_db_and_tabl(database_name)
        print("Для работы с базой данных запустите на своем ПК программу pgAdmin4,\n"
              "Нажмите правой кнопкой мышки на надписть PostgreSQL и выберете из выпадающего списка комнду Refresh.\n"
              "Сразу после обновления списка появится созданная Вами база данных с Вашим названием\n"
              "Нажмите на название Вашей базы данных левой кнопкой мышки для ее выбора и активации")


def working_with_the_database():
    print("Теперь перейдем к заполнению Вашей базы данных информацией о работодателях и их вакансиях")
    while True:
        print("Для начала работы с данными введите цифру 1\n"
              "Для завершения работы с программой введите цифру 2")
        choice = input("Введите выбранный Вами вариант: ")
        if choice == '1':
            return 1
        elif choice == '2':
            print("Всего вам хорошего! Благодарим за использование данной программы.")
            break
        else:
            print("Вы сделали не правильный выбор. Попробуйте еще раз.\n")


def data_entry():
    if working_with_the_database() == 1:
        db_input = input("Введите название вашей базы данных: ")
        employer_input = input("Введите название компании, для получения вакансий,\n"
                               "Например Carprice: ")
        if db_input:
            #if employer_input:
                insert_data(db_input, employer_input)
                print(f"Данные о {employer_input}, а так же вакансиях компании успешно добавлены")
            #else:
                #print("Название компании не введено!")
        else:
            print("Название базы данных не введено!")


def user_interaction():
    print("Получение информацию из базы данных.")
    while True:
        print("Для продолжения работы введите цифру 1.\n"
              "Для выхода из программы введите цифру 2.\n")
        choice = input("Введите цифру: ")
        if choice == '1':
            db_name = input("Введите название базы данных: ")
            db_manager = DBManager(db_name)
            job_options = "Для выхода из программы нажмите '1'\n" \
                          "Для получения списка всех компаний и количества вакансий у каждой компании нажмите '2'\n" \
                          "Для получения списка всех вакансий с указанием названия компании," \
                          " названия вакансии и зарплаты и ссылки на вакансию нажмите '3'\n" \
                          "Для получения средней зарплаты по вакансиям нажмите '4'\n" \
                          "Для получения списка всех вакансий," \
                          " у которых зарплата выше средней по всем вакансиям нажмите '5'\n" \
                          "Для получения списка всех вакансий," \
                          " в названии которых содержатся переданные в метод слова, нажмите '6'\n" \
                          "Для возврата в меню, нажмите '0'"
            print(job_options)
            while True:
                user_input = input("Выбор запроса: ")
                if user_input == '1':
                    print("Всего вам хорошего! Благодарим за использование данной программы.")
                    break
                elif user_input == '2':
                    db_manager.get_companies_and_vacancies_count()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '3':
                    db_manager.get_all_vacancies()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '4':
                    db_manager.get_avg_salary()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '5':
                    db_manager.get_vacancies_with_higher_salary()
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '6':
                    user_input = input()
                    db_manager.get_vacancies_with_keyword(user_input)
                    print("Запрос осуществлен, для возврата в меню нажмите '0'")
                elif user_input == '0':
                    print(job_options)
                else:
                    print("Неверное значение! Введите цифру от 1-6!")
        elif choice == '2':
            print("Всего вам хорошего! Благодарим за использование данной программы.")
            break
        else:
            print("Вы сделали не правильный выбор. Попробуйте еще раз.\n")


def main():
    creating_a_user_database()
    data_entry()
    user_interaction()
