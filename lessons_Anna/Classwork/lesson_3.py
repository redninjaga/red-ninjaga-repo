import tkinter as tk
from tkinter import messagebox

def calculator():
    num_1 = float(entry_1.get())
    num_2 = float(entry_2.get())
    action = radio.get()
    if action == 1:
        rezult = num_1 + num_2
    elif action == 2:
        rezult = num_1 - num_2
    elif action == 3:
        rezult = num_1 * num_2
    elif action == 4:
        if num_2 != 0:
            rezult = num_1 / num_2
        else:
            messagebox.showerror("Помилка", "/ на 0 неможливо!")
        return
    messagebox.showinfo("Результат", f"Результат: {rezult}")

window = tk.Tk()
window.title("Radiobutton")
window.geometry("300x400")
window["bg"] = "#33F0FF"

entry_1 = tk.Entry(window)
entry_1.pack()
entry_2 = tk.Entry(window)
entry_2.pack()

radio = tk.IntVar()
radio_1 = tk.Radiobutton(window, text="+", variable=radio, value=1, bg="#33F0FF")
radio_2 = tk.Radiobutton(window, text="-", variable=radio, value=2, bg="#33F0FF")
radio_3 = tk.Radiobutton(window, text="*", variable=radio, value=3, bg="#33F0FF")
radio_4 = tk.Radiobutton(window, text="/", variable=radio, value=4, bg="#33F0FF")

radio_1.pack()
radio_2.pack()
radio_3.pack()
radio_4.pack()

btn = tk.Button(window, text="Обчислити", command=calculator)
btn.pack()

window.mainloop()
