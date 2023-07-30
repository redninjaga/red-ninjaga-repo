from tkinter import *
from tkinter import font

def font_give():
    gived_font = font_var.get()

    if gived_font == "Monaco":
        my_font = font.Font(family="Monaco", size=16, weight="bold")
    elif gived_font == "Times New Roman":
        my_font = font.Font(family="Times New Roman", size=20, slant="italic")
    elif gived_font == "Georgia":
        my_font = font.Font(family="Georgia", size=25, weight="normal")
    elif gived_font == "Garamond":
        my_font = font.Font(family="Garamond", size=28, overstrike=True)
    elif gived_font == "Jokerman":
        my_font = font.Font(family="Jokerman", size=100, underline=True)

    font_label.configure(font=my_font)

window = Tk()
window.title("")
window.geometry("500x600")
window["bg"] = "#41e0c3"

font_var = StringVar()

font_label = Label(window, text="Game_over", font=("Arial", 12), bg="#41e0c3")
font_label.pack()

font_1_radio = Radiobutton(window, text="Monaco", variable=font_var, value="Monaco", bg="#41e0c3")
font_1_radio.pack()

font_2_radio = Radiobutton(window, text="Times New Roman", variable=font_var, value="Times New Roman", bg="#41e0c3")
font_2_radio.pack()

font_3_radio = Radiobutton(window, text="Georgia", variable=font_var, value="Georgia", bg="#41e0c3")
font_3_radio.pack()

font_4_radio = Radiobutton(window, text="Garamond", variable=font_var, value="Garamond", bg="#41e0c3")
font_4_radio.pack()

font_5_radio = Radiobutton(window, text="Jokerman", variable=font_var, value="Jokerman", bg="#41e0c3")
font_5_radio.pack()

btn = Button(window, text="Submit", command=font_give, bg="#41e0c3")
btn.pack()

window.mainloop()
