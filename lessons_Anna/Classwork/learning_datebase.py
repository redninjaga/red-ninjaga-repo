import sqlite3
from colorama import *
init(autoreset=True)


def delete_and_payment_car():
    cost = 5
    input_number = input("Write number of your car: ")
    cursor.execute(f"SELECT * FROM parking WHERE number = '{input_number}'")
    result = cursor.fetchone()
    if result:
        cursor.execute(f"DELETE FROM parking WHERE number = '{input_number}'")
        connection.commit()
        print(f"Мы рады что вы были у нас, вы пробыли на парковке: {result[2]} часов, стоимость: {cost * result[2]}$")
    else:
        print(Fore.LIGHTRED_EX + "Cars with number not found")


def add_parking():
    run = True
    while run:
        input_number = input("Write number of your car: ")
        cursor.execute(f"SELECT number FROM parking WHERE number = '{input_number}'")
        result_number = cursor.fetchone()
        if result_number:
            print(Fore.LIGHTRED_EX + "This car is parking yet")
            print(
                "if you want change time your car, write " + Fore.LIGHTCYAN_EX + 'time' + Style.RESET_ALL + "\nelse if your number is not correct write " + Fore.LIGHTCYAN_EX + 'again')
            answer = input("Your answer: ")
            if answer == "time":
                time = int(input("Enter time: "))
                cursor.execute(f"UPDATE parking SET time = {time}")
                connection.commit()
                break
            if answer == "again":
                continue
        print(result_number)
        input_time = int(input("Write time, which you want stay: "))
        input_model = input("Write model of your car: ")

        if input_time > 0:
            cursor.execute("INSERT INTO parking (number, time, model) VALUES (?, ?, ?)", (input_number, input_time, input_model))
            connection.commit()
            print("Your car is parking successfully ")
            run = False
        else:
            print(Fore.LIGHTRED_EX + "\nYou need again write the time, which more than zero\n")
            continue


def functions():
    run = True
    while run:
        print("1) You need parking of your car \n2) Locking of all cars in the park \n3) Search car in the model \n4) Delete all cars")
        select = int(input(Fore.LIGHTCYAN_EX + Back.LIGHTMAGENTA_EX + Style.BRIGHT + "Your answer: "))
        print(f"{'-' * 20}")
        if select == 1:
            add_parking()
        elif select == 2:
            cursor.execute("SELECT * FROM parking")
            results = cursor.fetchall()
            for result in results:
                print(f"id: {result[0]} \nnumbers: {result[1]} \ntime: {result[2]} \nmodel: {result[3]} \n{'-' * 20}")
            if results == 0:
                print("Parking haven't cars")
        elif select == 3:
            model_input = input("Write your model of the car ")
            cursor.execute(f"SELECT * FROM parking WHERE model = '{model_input}'")
            results = cursor.fetchall()
            for result in results:
                print(f"id: {result[0]} \nnumbers: {result[1]} \ntime: {result[2]}")
        elif select == 4:
            delete_and_payment_car()
        else:
            print("Данные введены не корректно попробуйте снова")


connection = sqlite3.connect("parking.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS parking 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT,
time INTEGER,
model TEXT)
""")
connection.commit()
# cursor.execute("INSERT INTO parking (number, time, model) VALUES (?, ?, ?)", ("AB23", 2, "NISSAN E1"))
# connection.commit()
# print"("Car add")"

functions()

# cursor.execute("SELECT * FROM parking WHERE model = 'NISSAN E1'")
# results = cursor.fetchall()
# # print(results)

