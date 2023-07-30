from tkinter import *
from tkinter import messagebox

def check():
    if check_1.get() == 1:
        messagebox.showinfo("", "Ты нажал на 1")
    elif check_2.get() == 1:
        messagebox.showinfo("", "Ты нажал на 2")
    else:
        messagebox.showinfo("", "Ты нажал на 1 и 2")

window = Tk()
window.title("checkbutton")
window.geometry("300x400")
window["bg"] = "#33F0FF"

check_1 = IntVar()
checkbutton = Checkbutton(window, text="text_1", variable=check_1, bg="#33F0FF")
checkbutton.pack()
check_2 = IntVar()
checkbutton = Checkbutton(window, text="text_2", variable=check_2, bg="#33F0FF")
checkbutton.pack()

btn = Button(window, text="Если выбрал нажымай", command=check, bg="#33F0FF")
btn.pack()

window.mainloop()