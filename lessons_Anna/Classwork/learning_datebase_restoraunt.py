import sqlite3

connection = sqlite3.connect("restoraunt.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS restoraunt 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
people INTEGER,
name TEXT,
time INTEGER,
phone INTEGER) 
""")
connection.commit()


