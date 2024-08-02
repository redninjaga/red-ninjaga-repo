import sqlite3


# def add_tables():
#     run = True
#     while run:
#         print("If you want to check all the tables, write in 'Number table' check")
#         input_number = input("Number table: ")
#         if input_number == "check":
#             cursor_table.execute("SELECT * FROM tables")
#             results = cursor_table.fetchall()
#             for result in results:
#                 print(f"id: {result[0]} \nnumbers: {result[1]} \nmax_people: {result[2]} \n{'-' * 20}")
#         input_max_people = input("Max people: ")
#         cursor_table.execute("INSERT INTO tables (number, max_people) VALUES (?, ?)", (input_number, input_max_people))
#         connection_table.commit()


def people_of_table():
    input_number = input("Write number of table: ")
    cursor_table.execute(f"SELECT number FROM tables WHERE number = '{input_number}'")
    results = cursor_table.fetchall()

    cursor_table.execute("SELECT * FROM tables")
    results = cursor_table.fetchall()

    while not results:
        print(f"Our restoraunt haven't {input_number} table, we have ")
        for result in results:
            print(f"id: {result[0]} \nnumbers: {result[1]} \npeople: {result[2]} \n{'-' * 20}")
        input_number = input("Write number of table: ")
        cursor_table.execute(f"SELECT number FROM tables WHERE number = '{input_number}'")
        results = cursor_table.fetchall()
    input_people = input("Write how many people go to the table: ")


connection_restoraunt = sqlite3.connect("restoraunt.db")
cursor_restoraunt = connection_restoraunt.cursor()
cursor_restoraunt.execute("""
CREATE TABLE IF NOT EXISTS restoraunt 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
people INTEGER,
name TEXT,
time INTEGER,
phone INTEGER) 
""")
connection_restoraunt.commit()

connection_table = sqlite3.connect("tables.db")
cursor_table = connection_table.cursor()
cursor_table.execute("""
CREATE TABLE IF NOT EXISTS tables 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
number INTEGER,
max_people INTEGER)
""")
connection_table.commit()

people_of_table()
