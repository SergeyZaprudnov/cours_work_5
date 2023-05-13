from base.database_creation import create_db_and_tabl
from base.insert_db import inert_data
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
            print("Всего Вам хорешего. Благодарим за использовние данной программы.")
            break
        else:
            print("Вы сделали не правильный выбор, попробуйте еще раз\n")

def creating_a_user_database():
    if start_of_the_program() == 1:
        database_name = input("Введите название Вашей базы данных: ").lower()
        create_db_and_tabl(database_name)
        print("Для работы с базой данных запустите на своем ПК программу pgAdmin4,\n"
              "Нажмите правой кнопкой мышки на надписть PostgreSQL и выберете из выпадающего списка комнду Refresh.\n"
              "Сразу после обновления списка появится созданная Вами база данных с Вашим названием\n"
              "Нажмите на название Вашей базы данных левой кнопкой мышки для ее выбора и активации")


start_of_the_program()