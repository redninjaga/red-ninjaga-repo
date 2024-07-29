import telebot
import random

bot = telebot.TeleBot("7094056252:AAFGML3l0hKOcGP1lPtSaakfSJNL0geFACo")

games = {}


def generate_secret_number():
    return ''.join(random.sample('0123456789', 4))


def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    return bulls, cows


@bot.message_handler(commands=['start'])
def start_game(message):
    user_id = message.from_user.id
    secret_number = generate_secret_number()
    games[user_id] = secret_number
    bot.reply_to(message, "Игра началась! Отгадайте четырехзначное число. Удачи!")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id not in games:
        bot.reply_to(message, "Сначала начните игру командой /start")
        return

    secret_number = games[user_id]
    guess = message.text.strip()

    if not guess.isdigit() or len(guess) != 4:
        bot.reply_to(message, "Введите четырехзначное число.")
        return

    bulls, cows = count_bulls_and_cows(secret_number, guess)

    if bulls == 4:
        bot.reply_to(message, f"Поздравляю! Вы угадали число {secret_number}. Ваша победа!")
        del games[user_id]  # Удаляем игру из активных игр
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
