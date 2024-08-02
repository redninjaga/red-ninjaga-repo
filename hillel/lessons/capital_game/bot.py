import telebot
import random
from capitals import capitals

bot = telebot.TeleBot('7227984936:AAEXL3CfZn9PVGO1_uYI6UC3RNQNRpWq9gA')

# глобальні змінні
capital = ''
point = 0


@bot.message_handler(commands=['start', 'help', 'start_game', 'stop_game'])
def get_commands(message):
    if message.text == '/start':
        bot.reply_to(message, f'Hello, {message.from_user.first_name}!\n'
                              f'This is game \'Capital - country\'')
        start_game(message)

    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Commands:\n'
                                          '/start_game - start the game\n'
                                          '/stop_game - stop the game')

    elif message.text == '/start_game':
        send_capital(message)

    elif message.text == '/stop_game':
        get_point(message)
        start_game(message)


def start_game(message):
    bot.send_message(message.chat.id, '/start_game - start the game\n')


def get_point(message):
    global point
    bot.send_message(message.chat.id, f'Points: {point}')
    point = 0


def choice_capital():
    all_capital = list(capitals.keys())
    rand_capital = random.choice(all_capital)
    return rand_capital


def send_capital(message):
    global capital
    capital = choice_capital()
    bot.send_message(message.chat.id, f'Capital: {capital}')

    # фіксуємо запит від користувача та відправляємо у функцію
    bot.register_next_step_handler(message, get_country)


def get_country(message):
    global point

    if message.text in ['/help', '/stop_game']:
        get_commands(message)
        return

    user_answer = message.text.title()
    right_answer = capitals[capital]

    if user_answer == right_answer:
        point += 1
        bot.send_message(message.chat.id, 'Right')
    else:
        point -= 1
        bot.send_message(message.chat.id, 'Wrong')

    send_capital(message)


@bot.message_handler(content_types=['text'])
def get_text(message):
    get_country(message)


bot.infinity_polling()