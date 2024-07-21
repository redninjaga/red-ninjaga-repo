import telebot
import random

bot = telebot.TeleBot('7367864457:AAEref5cyakkd-B5FNzB84u38ZsPtOrgvBg')

# Словник з питаннями та відповідями
answer_dict = {
    "Як справи?": ["Добре, дякую!", "Все чудово, а у вас?", "Не дуже, але тримаюсь."],
    "Яка погода за вікном?": ["Сонячно!", "Падає дощ.", "Хмарно і холодно."],
    "Як тебе звати?": ["Мене звати Бот.", "Я ваш віртуальний помічник.", "Я просто бот без імені."],
    "Скільки тобі днів?": ["Я народився сьогодні!", "Мені всього кілька днів.", "Я існую вічно."],
    "Котра година?": ["Вибачте, я не знаю часу.", "Подивіться на свій годинник.", "Зараз саме час насолоджуватись життям!"]
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вітаю! Як я можу допомогти?")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Ось список можливих питань:\n" + "\n".join(answer_dict.keys())
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    if user_message in answer_dict:
        response = random.choice(answer_dict[user_message])
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Вибачте, я не знаю відповіді на це питання.")


bot.polling()
