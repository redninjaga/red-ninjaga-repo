import random
from tkinter import *

def play_game(user_choice):
    choice = ["Rock", "scissors", "paper"]
    computer_choice = random.choice(choice)
    rezult = winner(user_choice, computer_choice)
    label.config(text=f"Твой выбор: {user_choice}\n выбор компюнтера {computer_choice}\n Результат {rezult}")
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ничья"
    elif (user_choice == "Rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "Rock"):
        return "Ты победил"
    else:
        return "Компюнтер победил"
window = Tk()
window.title("rock,scissors,paper")
window.geometry("400x500")
window["bg"] = "#33F0FF"

choice = ["Rock", "scissors", "paper"]
choice_button = [""]

for choice in choice:
    button = Button(window, text=choice, command=lambda c=choice: play_game(c), bg="#33F0FF")
    button.pack()
    choice_button.append(button)
    label = Label(window)
    label.pack()

window.mainloop()
