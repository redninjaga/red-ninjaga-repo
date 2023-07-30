import tkinter as tk

def text():
    entry_text = int(entry.get())
    entry1_text = int(entry_1.get())

    suma = entry_text + entry1_text

    label.config(text="Результат: " + str(suma))

#створення вікна
window = tk.Tk()
window.title("Приклад")
window.geometry("300x300")

label = tk.Label(window, text="Число_1")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()
label_1 = tk.Label(window, text="Число_2")
label_1.pack(pady=10)
entry_1 = tk.Entry(window)
entry_1.pack()
#створення кнопки
button = tk.Button(window, text="Класти", command=text)
button.pack(pady = 10)

window.mainloop()