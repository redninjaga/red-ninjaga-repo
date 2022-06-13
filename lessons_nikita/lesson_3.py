input_number = int(input("Введите число"))

last_number = int(input_number % 10)
two_number = int(input_number / 10)
result = int(last_number * 100 + two_number)
print(result)
