# Author Maksim Derevianko
import string

# 1
print("---Task 1---")
import math


def square(side: float) -> (float, float, float):
    """Calculates the perimeter, area, and diagonal of a square along a given side."""
    perimeter = 4 * side
    area = side ** 2
    diag = math.sqrt((side ** 2) + (side ** 2))
    return round(perimeter, 2), round(area, 2), round(diag, 2)


user_input = float(input("Введіть сторону квадрата: "))
print(f"Периметр, площа, діагональ: {square(user_input)}")

# 2
print("---Task 2---")


def reverse(text: str) -> (str):
    """The function returns the text in an inverted form without punctuation marks and spaces"""
    reversed_text = text[::-1]
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ '
    for char in punctuation:
        reversed_text = reversed_text.replace(char, "")
    return reversed_text


user_input = input("Введіть текст: ")
print(f"Перевернутий текст без розділових знаків та пробілів: {reverse(user_input)}")

# 3
print("---Task 3---")


def hypotenuse(a: float, b: float) -> (float):
    """The function returns the length of the hypotenuse calculated by the Pythagorean theorem."""
    hypoten = math.sqrt((a ** 2) + (b ** 2))
    return round(hypoten, 2)


user_a = float(input("Введіть довжину катету а: "))
user_b = float(input("Введіть довжину катету b: "))
print(f"Довжина гіпотенузи: {hypotenuse(user_a, user_b)}")
