import random


def generate_unique_number(length):
    digits = '0123456789'

    number = ''.join(random.sample(digits, length))
    return number

def count_bulls_and_cows(secret, guess):
    """
    Метод count_bulls_and_cows используется для подсчета количества "быков" и "коров" в игре "Бык и корова". Давайте разберем его по шагам:

    Подсчет "быков":
    bulls = sum(s == g for s, g in zip(secret, guess))
    Эта строка создает пару символов из секретного числа (secret) и предполагаемого числа (guess) с помощью функции zip. Затем она сравнивает каждый символ в паре и, если они совпадают, прибавляет 1 к сумме. Таким образом, bulls будет содержать количество цифр, которые совпадают по значению и по позиции.

    Подсчет "коров":
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    Эта строка выполняет следующее:

    Создает множество уникальных цифр из предполагаемого числа (set(guess)), чтобы исключить повторения.
    Для каждой уникальной цифры считает количество ее вхождений в секретное число и в предполагаемое число с помощью secret.count(digit) и guess.count(digit).
    Берет минимум из этих двух значений, чтобы учесть только те вхождения, которые могут быть "коровами".
    Суммирует минимальные значения для всех уникальных цифр.
    Вычитает количество "быков" из этой суммы, чтобы исключить те цифры, которые уже были учтены как "быки".
    Возвращение результата:

    return bulls, cows
    Метод возвращает количество "быков" и "коров" в виде кортежа.

    Пример
    Допустим, секретное число - 123, а предположение - 135.

    "Быки": 1 на первой позиции совпадает, поэтому bulls = 1.
    "Коровы": уникальные цифры из предположения - 1, 3, 5. Цифра 1 уже учтена как "бык". Цифра 3 есть в секретном числе, поэтому добавляется одна "корова". Цифры 5 нет в секретном числе. Таким образом, cows = 1.
    В результате, для secret = 123 и guess = 135, метод count_bulls_and_cows вернет (1, 1).
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls #поменяти цю строку
    return bulls, cows


def play_game():
    print("Добро пожаловать в игру 'Бык и корова'!")

    secret_number = generate_unique_number(3)
    print(f"Загаданное уникальное число с 3 цифрами: {secret_number}")

    attempts = 0
    while True:
        guess = input("Введите вашу попытку (три цифры): ").strip()

        if not guess.isdigit() or len(guess) != 3:
            print("Введите именно трёхзначное число.")
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret_number, guess)

        if bulls == 3:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break
        else:
            print(f"{bulls} быков и {cows} коров. Попробуйте снова!")


play_game()
