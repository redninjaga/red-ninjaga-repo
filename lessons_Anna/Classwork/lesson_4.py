from tkinter import *
from tkinter import messagebox

def check():
    if check_1.get() == 1:
        messagebox.showinfo("", "Нажат")
    else:
        messagebox.showinfo("", "Не нажат")

window = Tk()
window.title("checkbutton")
window.geometry("300x400")
window["bg"] = "#33F0FF"

check_1 = IntVar()
checkbutton = Checkbutton(window, text="text", variable=check_1)
checkbutton.pack()

btn = Button(window, text="Если выбрал нажымай", command=check, bg="#33F0FF")
btn.pack()

window.mainloop()
