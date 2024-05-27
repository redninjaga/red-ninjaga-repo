# Author Maksim Derevianko

# 1
import random

random_numbers = [random.randint(1, 10) for _ in range(10)]

even_numbers = [num for num in random_numbers if num % 2 == 0]
max_even = max(even_numbers) if even_numbers else None

odd_numbers = [num for num in random_numbers if num % 2 != 0]
min_odd = min(odd_numbers) if odd_numbers else None

print("Список випадкових чисел:", random_numbers)
print("Найбільший парний елемент:", max_even)
print("Найменший непарний елемент:", min_odd)

# 2
random_numbers = [random.randint(-10, 10) for _ in range(10)]

three_smallest_sum = sum(sorted(random_numbers)[:3])

print("Список випадкових чисел:", random_numbers)
print("Три найменші числа:", sorted(random_numbers)[:3])
print("Сума трьох найменших чисел:", three_smallest_sum)

# 3
grades_input = input("Введіть оцінки через пробіл (від 1 до 5): ")

grades = []
for grade in grades_input.split():
    try:
        grade_int = int(grade)
        if 1 <= grade_int <= 5:
            grades.append(grade_int)
        else:
            print(f"Оцінка {grade_int} не входить в діапазон від 1 до 5 і буде проігнорована.")
    except ValueError:
        print(f"'{grade}' не є дійсною оцінкою і буде проігноровано.")

if grades:
    success_rate = ((grades.count(3) + grades.count(4) + grades.count(5)) / len(grades)) * 100
    print(f"Успішність: {success_rate:.2f}%")
else:
    print("Не введено жодної дійсної оцінки.")

print("Дійсні оцінки:", grades)
