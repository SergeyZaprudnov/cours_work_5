from base.database_creation import create_db_and_tabl
from base.insert_db import insert_data
from base.db_manager import DBManager

def start_of_the_program():
    print("Добро пожаловать в программу по работе с базой данных PostgreSQL\n"
          "Программа позволяет получить сведения о работодателях, а так же, их вакансиях с интернет ресурса HeadHunter.\n"
          "Полученные Вами данные будут сохраняться в базу данных.\n"
          "Приятного Вам пользования!")

    while True:
        print("Если Вы хотите создать базу данных, введите цифру  1\n"
              "Если Вы хотите завершить работу с программой, введите цифру 2")
        choice = input("Ведите номер выбранного Вами варианта: ")
        if choice == "1":
            return 1
        elif choice == "2":
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
        if choice == "1":
            return 1
        elif choice == "2":
            print("Всего вам хорошего! Благодарим за использование данной программы.")
            break
        else:
            print("Вы сделали не правильный выбор. Попробуйте еще раз.\n")

def data_entry():
    if working_with_the_database() == 1:
        bd_input = input("Введите название вашей базы данных: ")
        employer_input = input("Введите название компании, для получения вакансий,\n"
                               "Например Carprice: ")
        if bd_input:
            if employer_input:
                insert_data(bd_input, employer_input)
                print(f"Данные о {employer_input}, а так же вакансиях компании успешно добавлены")
            else:
                print("Название компании не введено!")
        else:
            print("Название базы данных не введено!")
