import telebot
import random

bot = telebot.TeleBot('7075234021:AAHPoA8en0PY4UzFUKr5jhuHKGb9HOuvi6Y')

user_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, Lera!\nThis is math bot!\nDetails /help\nTo start the game send the command /start_game")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Commands:\n/start - Start bot\n/start_game - Start a new game\n/stop_game - Stop the current game")


@bot.message_handler(commands=['start_game'])
def start_game(message):
    user_data[message.chat.id] = {'correct': 0, 'incorrect': 0, 'total': 0}
    send_math_example(message.chat.id)


@bot.message_handler(commands=['stop_game'])
def stop_game(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        stats = user_data[chat_id]
        bot.send_message(chat_id, f"Result:\nRight: {stats['correct']}\nWrong: {stats['incorrect']}\nAmount expressions: {stats['total'] - 1}")
        del user_data[chat_id]
    bot.send_message(chat_id, "To start the game send the command /start_game")


def send_math_example(chat_id):
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    if operation == '/': num1 *= num2
    question = f"{num1} {operation} {num2}"
    user_data[chat_id]['current_answer'] = eval(question)
    user_data[chat_id]['total'] += 1
    bot.send_message(chat_id, question)


@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_answer(message):
    chat_id = message.chat.id
    try:
        user_answer = float(message.text)
        correct_answer = user_data[chat_id]['current_answer']
        if user_answer == correct_answer:
            user_data[chat_id]['correct'] += 1
            bot.send_message(chat_id, "Right!")
        else:
            user_data[chat_id]['incorrect'] += 1
            bot.send_message(chat_id, f"Wrong! The correct answer was {correct_answer}.")
        send_math_example(chat_id)
    except ValueError:
        bot.send_message(chat_id, "Use only digits and dot.")


bot.polling()
