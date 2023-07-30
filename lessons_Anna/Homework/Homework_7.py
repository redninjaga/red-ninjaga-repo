from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("Cars.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS car (id INTEGER PRIMARY KEY AUTOINCREMENT, marka TEXT, model TEXT)")

def append():
    marka = entry_1.get()
    model = entry_2.get()
    if marka and model:
        c.execute("INSERT INTO car (marka, model) VALUES (?, ?)", (marka, model))
        conn.commit()
        messagebox.showinfo("", "Машина добавлена")
        entry_1.delete(0, END)
        entry_2.delete(0, END)
    else:
        messagebox.showerror("", "Ошибка")

def show():
    c.execute("SELECT * FROM car")
    cars = c.fetchall()
    if cars:
        messagebox.showinfo("", "\n".join([f"{car[0]}. {car[1]} - {car[2]}" for car in cars]))
    else:
        messagebox.showinfo("", "У вас нету машын")

def delete():
    ID = entry_3.get()
    if ID:
        c.execute("DELETE FROM car WHERE id=?", (ID,))
        conn.commit()
        messagebox.showinfo("", "Машина удалена")
        entry_3.delete(0, END)
    else:
        messagebox.showerror("", "Ведите ID")

window = Tk()
window.title("checkbutton")
window.geometry("300x400")
window["bg"] = "#33F0FF"

label = Label(window, text="Марка машыны")
label.pack()

entry_1 = Entry(window)
entry_1.pack()

label_1 = Label(window, text="Модель машыны")
label_1.pack()

entry_2 = Entry(window)
entry_2.pack()

button = Button(window, text="Добавить машыну", command=append)
button.pack()

button_show = Button(window, text="Посмотреть список машын", command=show)
button_show.pack()

entry_3 = Entry(window)
entry_3.pack()

button_delete = Button(window, text="Удалить машыну", command=delete)
button_delete.pack()

window.mainloop()
