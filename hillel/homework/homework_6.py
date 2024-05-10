# Author: Maksym Derevianko

# 1
word = input("Введіть слово: ")
result = ""

if word.isalpha():
    for char in word:
        if char.lower() in "aeiou":
            result += "0"
        else:
            result += "1"
    print(result)
else:
    print("Введене слово має містити лише літери.")

# 2
sentence = input("Введіть рядок: ")

total_char_num = 0
digit_num = 0
upper_letter_num = 0
lower_letter_num = 0
other_symbol_num = 0

for char in sentence:
    total_char_num += 1
    if char.isdigit():
        digit_num += 1
    elif char.isupper():
        upper_letter_num += 1
    elif char.islower():
        lower_letter_num += 1
    else:
        other_symbol_num += 1

print("Total characters:", total_char_num)
print("Lower letters:", lower_letter_num)
print("Upper letters:", upper_letter_num)
print("Digits:", digit_num)
print("Other simbols:", other_symbol_num)

