import os
import random
import telebot

IMAGE_DIRS = {
    "природа": "C:/Max/PycharmProjects/red-ninjaga-repo/hillel/homework/telegram_bots_hillel/homework_22/nature",
    "люди": "C:/Max/PycharmProjects/red-ninjaga-repo/hillel/homework/telegram_bots_hillel/homework_22/people",
    "космос": "C:/Max/PycharmProjects/red-ninjaga-repo/hillel/homework/telegram_bots_hillel/homework_22/space"
}

bot = telebot.TeleBot("7475402794:AAEKrd_QZBwSJwgb9ddQu6mAWV6bQsrkJjY")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Напиши мне категорию: "природа", "люди" или "космос".')


@bot.message_handler(func=lambda message: True)
def send_random_image(message):
    text = message.text.lower()

    category = None
    for key in IMAGE_DIRS.keys():
        if key in text:
            category = key
            break

    if not category:
        bot.reply_to(message, 'Я не понимаю эту категорию. Попробуй еще раз: "природа", "люди" или "космос".')
        return

    image_dir = IMAGE_DIRS.get(category)
    images = os.listdir(image_dir)
    if not images:
        bot.reply_to(message, 'Ошибка: Нет изображений в этой категории.')
        return

    image_path = os.path.join(image_dir, random.choice(images))
    with open(image_path, 'rb') as image_file:
        bot.send_photo(message.chat.id, image_file)


bot.infinity_polling()
