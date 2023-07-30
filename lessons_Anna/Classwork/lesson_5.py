from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def show_message():
    food = ""
    if burger.get():
        food += "Burger\n"
    if hot_dog.get():
        food += "Hot_dog\n"
    if pizza.get():
        food += "Pizza\n"
    if food:
        messagebox.showinfo("", "Ваш выбор: \n" + food)
    else:
        messagebox.showwarning("", "Пожалуйста выберите что-то из списка")

window = Tk()
window.title("Cafe")
window.geometry("400x500")

burger = IntVar()
pizza = IntVar()
hot_dog = IntVar()

burger_img = Image.open("burger.png")
hot_dog_img = Image.open("hot_dog.png")
pizza_img = Image.open("pizza.png")

image_size = (80, 80)
burger_img = burger_img.resize(image_size)
pizza_img = pizza_img.resize(image_size)
hot_dog_img = hot_dog_img.resize(image_size)

burger_image = ImageTk.PhotoImage(burger_img)
pizza_image = ImageTk.PhotoImage(pizza_img)
hot_dog_image = ImageTk.PhotoImage(hot_dog_img)

burger_check = Checkbutton(window, text="burger", variable=burger, image=burger_image, compound=RIGHT, padx=10)
burger_check.pack()
pizza_check = Checkbutton(window, text="pizza", variable=pizza, image=pizza_image, compound=RIGHT, padx=10)
pizza_check.pack()
hot_dog_check = Checkbutton(window, text="hot_dog", variable=hot_dog, image=hot_dog_image, compound=RIGHT, padx=10)
hot_dog_check.pack()

button = Button(window, text="Submit", command=show_message, bg="blue", fg="white", font=("Arial", 14, "bold"), padx=10)
button.pack()

mainloop()
