# Author: Maksym Derevianko
# 1
import sys

print("Программа перевіряє, чи ділиться введене число на 7.")
input_1 = input("Введіть трьохзначне число: ")

if len(input_1) > 3 or len(input_1) < 3:
    print("Помилка. Число має бути трьохзначне.")
    sys.exit()
not_last = int(input_1[0:2])
double_last = int(input_1[2]) * 2
difference = not_last - double_last
print(f"Число {input_1} без останьой цифри {not_last}")
print(f"Подвоєна остання цифра {input_1[2]} дорівнює {double_last}")
print(f"Різниця {not_last} - {double_last} = {difference}")
if difference % 7 == 0:
    print(f"Число {difference} кратно 7")
    print(f"Число {input_1} кратно 7")
else:
    print(f"Число {difference} не кратно 7")
    print(f"Число {input_1} не кратно 7")

# 2
input_2 = input("Введіть слово: ")
reversed_input_2 = input_2[::-1]

if input_2 == reversed_input_2:
    print(f"'{input_2}' це паліндром")
else:
    print(f"'{input_2}' це не паліндром")
