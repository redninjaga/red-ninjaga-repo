# Author: Maksim Derevianko

# 1
print("---Task 1---")
amount = int(input("Enter price: "))

while amount % 2 == 0:
    amount /= 2

print(f"To pay: {amount}")

# 2
print("---Task 2---")
number = int(input("Enter number (1-9): "))

if 1 <= number <= 9:
    for i in range(1, 11):
        print(f"{i} * {number} = {number * i}")
else:
    print("Error! Number should be 1-9.")
