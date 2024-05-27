# Author: Maksym Derevianko

# 1
import random

even_random_numbers = []
for _ in range(10):
    even_random_numbers.append(random.choice(range(2, 101, 2)))

print("Список випадкових парних чисел:", even_random_numbers)

# 2
random_numbers = []
for _ in range(20):
    random_numbers.append(random.randint(-20, 20))

positive_numbers = []
negative_numbers = []

for num in random_numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

print(random_numbers)
print("positive number:", positive_numbers)
print("negative_number:", negative_numbers)

# 3
games_list = []

while True:
    game_name = input("Enter game: ")

    if game_name == "0":
        break

    if game_name in games_list:
        print("This game in list games")
    else:
        games_list.append(game_name)

print(games_list)
