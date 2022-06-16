number = 1
kratnoe:int = 0

while number != 21:
    kratnoe = number % 3
    if kratnoe == 0:
        print(number, "число кратное трём")
    number = int(number + 1)