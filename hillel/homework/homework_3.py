# Author: Maksym Derevianko

# 1
name = input("Введіть ім'я: ")
patronymic = input("Введіть ім'я по батькові: ")

print(f"{name[0].upper()}.{patronymic[0].upper()}.")

# 2
random_word = input("Введіть рядок: ")

if random_word[-1].isdigit():
    print("Останній символ: digit")
else:
    print("Останній символ: letter")

# 3
input_1 = input("Введіть слово 1: ")
input_2 = input("Введіть слово 2: ")
input_3 = input("Введіть слово 3: ")

if len(input_1) >= len(input_2) and len(input_1) >= len(input_3):
    print("Найдовше слово:", input_1)
if len(input_2) >= len(input_1) and len(input_2) >= len(input_3):
    print("Найдовше слово:", input_2)
if len(input_3) >= len(input_1) and len(input_3) >= len(input_2):
    print("Найдовше слово:", input_3)
