from tkinter import *
from tkinter import messagebox
import tkinter as tk
def start ():
    if office.get() == 1:
        a = float(0.04)
        b = float(ukr_money.get())
        c = a*b
        messagebox.showinfo('Результат',c)
    elif office.get() == 2:
        a = float(0.05)
        b = float(ukr_money.get())
        c=a*b
        messagebox.showinfo('Результат',c)
    else:
        office.get()==3
        a=float(0.07)
        b=float(ukr_money.get())
        c=a*b
        messagebox.showinfo('Результат',c)
My_window = tk.Tk()
My_window.title('Задача 1')
My_window.geometry("500x500")
My_window["bg"] = "#d9c3b1"
Label1 = Label(text='Введіть кількість гривень:',
               fg='#e8dbd5',# я поставила інший колір щоб можна було побачити текст
               bg='#4a1904',
               justify=CENTER,
               font=18,
              # height=30 #Я також законментувала цю строчку, тому що воно виглядало інакше не як в прикладі
               )
Label1.pack()
ukr_money=tk.Entry(width=50)
ukr_money.pack(side=tk.TOP,
           pady=20,
           padx=20)
btn=Button(My_window,
           text="Порахувати",
           width=50,
           height=10,
           command=start,
           bg='#2e1910',
           fg='white'
           )
btn.pack(side=tk.BOTTOM, padx=50, pady=170)
office=IntVar()
office1=Radiobutton(My_window,
                    text='Долар США',
                    variable=office,
                    value=1,
                    fg='#584332',
                    font=16,
                    bg='#d9c3b1'
                    )
office1.place(x=100,y=90)
office2=Radiobutton(My_window,
                    text='Євро',
                    variable=office,
                    value=2,
                    fg='#584332',
                    font=16,
                    bg='#d9c3b1'
                    )
office2.place(x=100,y=130)
office3=Radiobutton(My_window,
                    text='Англійський фунт',
                    variable=office,
                    value=3,
                    fg='#584332',
                    font=16,
                    bg='#d9c3b1'
                    )
office3.place(x=100,y=170)
My_window.mainloop()

