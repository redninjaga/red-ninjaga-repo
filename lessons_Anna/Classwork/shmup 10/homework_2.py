# Author: Maksym Derevianko

# 1
random_month = input()
if random_month in ("October", "September", "November", "11", "10" "9"):
    print("This is fall")
if random_month in ("December", "January", "February", "12", "1", "2"):
    print("This is winter")
if random_month in ("March", "April", "May", "3", "4", "5"):
    print("This is spring")
if random_month in ("June", "July", "August", "6", "7", "8"):
    print("This is summer")
else:
    print("This is not month")

# 2
price = int(input("Price: "))
time = int(input("Time: "))

if time >= 8 and time <= 19:
    print("Разом до сплати", price)
elif time >= 20 and time <= 22:
    print("Разом до сплати", price / 2)
else:
    print("Магазин не працює!")
