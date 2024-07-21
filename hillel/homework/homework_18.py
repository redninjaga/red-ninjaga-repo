# Author: Maksim Derevianko

# 1
print("---Task 1---")


def get_avg(array: list) -> float:
    return sum(array) / len(array)


def calculate_average_grades(grades: dict) -> dict:
    avg_grades = {}
    for record in grades:
        avg_grades[record] = get_avg(grades.get(record))
    return avg_grades


grades = {
    'Alice': [100, 90, 80],
    'Bob': [60, 70, 80],
    'Charlie': [80, 80, 80],
    'Dave': [70, 70, 70],
    'Eve': [60, 60, 60],
    'Frank': [50, 50, 50],
    'Gina': [40, 40, 40],
    'Hannah': [30, 30, 30],
    'Igor': [20, 20, 20],
    'Jenny': [10, 10, 10]
}

average_grades = calculate_average_grades(grades)
print(average_grades)

# 2
print("---Task 2---")


def count_digits(line: str) -> dict:
    result = {}
    for char in line:
        digit = int(char)
        if digit not in result:
            result[digit] = 1
        else:
            result[digit] = result.get(digit) + 1

    return result


print(count_digits('1233213231'))