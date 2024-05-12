# Author: Maksym Derevianko

# 1
while True:
    number = input("Введіть трьохзначне число: ")

    if len(number) != 3 or not number.isdigit():
        print("Будь ласка, введіть коректне трьохзначне число.")
        continue

    number = int(number)
    last_digit = number % 10
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)

    if last_digit % 2 == 0 and sum_digits % 3 == 0:
        if number % 6 == 0:
            print(f"Число {number} ділиться на 6.")
        else:
            print(f"Число {number} не ділиться на 6.")
        break
    else:
        print(f"Число {number} не відповідає умовам.")

