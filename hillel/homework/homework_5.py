# Author: Maksym Derevianko

# 1
print("---Task 1---")
total_sum = 0
amount = 0

while True:
    number = int(input("Введіть число: "))
    if number == 0:
        break
    total_sum += number
    amount += 1

if amount > 0:
    average = total_sum / amount
    print(f"Amount: {amount}")
    print(f"Sum numbers: {total_sum}")
    print(f"Average: {average}")
else:
    print("You didn't write valid number")

# 2
print("---Task 2---")
start = int(input("Enter start number: "))
current_number = start
end = int(input("Enter end number: "))
total_sum = 0

while current_number <= end:
    total_sum += current_number
    current_number += 1

print(f"Sum number from {start} to {end} = {total_sum}")
