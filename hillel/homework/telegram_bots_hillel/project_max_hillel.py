import telebot
import random

bot = telebot.TeleBot("7202962590:AAG3pXXGfJ18OzI2ha7Z82mlyzIKZPqKyYM")

games = {}


def generate_secret_number(length):
    return ''.join(random.sample('0123456789', length))


def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    return bulls, cows


@bot.message_handler(commands=['start'])
def start_game(message):
    bot.reply_to(message, "Выберите длину числа от 3 до 6 цифр.")


@bot.message_handler(func=lambda message: message.text.isdigit() and int(message.text) in range(3, 7))
def set_game_length(message):
    user_id = message.from_user.id
    length = int(message.text)
    secret_number = generate_secret_number(length)
    games[user_id] = {'secret_number': secret_number, 'length': length}
    bot.reply_to(message, f"Игра началась! Отгадайте {length}-значное число. Удачи!")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id not in games:
        bot.reply_to(message, "Сначала начните игру командой /start")
        return

    game = games[user_id]
    secret_number = game['secret_number']
    guess = message.text.strip()

    if not guess.isdigit() or len(guess) != game['length']:
        bot.reply_to(message, f"Введите {game['length']}-значное число.")
        return

    bulls, cows = count_bulls_and_cows(secret_number, guess)

    if bulls == game['length']:
        bot.reply_to(message, f"Поздравляю! Вы угадали число {secret_number}. Ваша победа!")
        del games[user_id]
    else:
        bot.reply_to(message, f"{bulls} быков и {cows} коров. Попробуйте снова!")


@bot.message_handler(commands=['stop'])
def stop_game(message):
    user_id = message.from_user.id
    if user_id in games:
        del games[user_id]
        bot.reply_to(message, "Игра остановлена.")
    else:
        bot.reply_to(message, "Вы не играете в игру в данный момент.")


bot.polling()
