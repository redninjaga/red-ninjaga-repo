# Author: Maksym Derevianko

# 1
total_sum = 0

for num in range(100, -1, -1):
    if num % 5 == 0:
        total_sum += num

print("Сума чисел кратних 5 від 100 до 0:", total_sum)

# 2
total_grades = int(input("Enter amount marks: "))

five_count = 0

for _ in range(total_grades):
    grade = int(input("Enter mark: "))
    if grade == 5:
        five_count += 1

percentage = (five_count / total_grades) * 100

print("Відсоток отриманих п'ятірок: {}%".format(round(percentage, 2)))
