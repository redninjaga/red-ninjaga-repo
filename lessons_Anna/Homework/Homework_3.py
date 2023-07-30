import tkinter as tk
from tkinter import messagebox

def answer():
    if radio.get() == 1:
        messagebox.showerror("Уведомление", "Ошибка")
    elif radio.get() == 2:
        messagebox.showerror("Уведомление", "Ошибка")
    elif radio.get() == 3:
        messagebox.showerror("Уведомление", "Ошибка")
    else:
        messagebox.showinfo("Уведомление", "Правильно")

window = tk.Tk()
window.title("Radiobutton")
window.geometry("300x400")
window["bg"] = "#33F0FF"

label_1 = tk.Label(window, text="Сколько процентов воды в теле человека", bg="#33F0FF")
label_1.pack()

radio = tk.IntVar()
radio_1 = tk.Radiobutton(window, text="65%", variable=radio, value=1, bg="#33F0FF")
radio_2 = tk.Radiobutton(window, text="80%", variable=radio, value=2, bg="#33F0FF")
radio_3 = tk.Radiobutton(window, text="50%", variable=radio, value=3, bg="#33F0FF")
radio_4 = tk.Radiobutton(window, text="70%", variable=radio, value=4, bg="#33F0FF")

radio_1.pack()
radio_2.pack()
radio_3.pack()
radio_4.pack()

btn = tk.Button(window, text="Ответить", command=answer)
btn.pack()

window.mainloop()
