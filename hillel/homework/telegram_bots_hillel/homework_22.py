import telebot
from telebot import types

bot = telebot.TeleBot("7476090657:AAGnWiWiWd0oGjH2gttdJ69ZW63QkGKy9yY")

COURSE_URLS = {
    'Front-end': 'https://lms.ithillel.ua/store/course/65d757a671c1a0061f0ec740',
    'Python': 'https://lms.ithillel.ua/store/course/5b9de7f9de1038dbaafc2e0d',
    'Java': 'https://lms.ithillel.ua/store/course/655ca24417d2c13c7f0824e4',
    'Дизайн': 'https://lms.ithillel.ua/store/course/65784fecec948961ac3d1143'
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f'Вітаю, {user_first_name}!\nПро школу ItHillel!',
        reply_markup=main_menu_keyboard()
    )


def main_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(course) for course in COURSE_URLS.keys()]
    markup.add(*buttons)
    return markup


def course_menu_keyboard(course_url):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Переходь!', url=course_url))
    return markup


@bot.message_handler(func=lambda message: message.text in COURSE_URLS)
def send_course_info(message):
    course_url = COURSE_URLS[message.text]
    bot.send_message(
        message.chat.id,
        f'Основи {message.text} для школярів',
        reply_markup=course_menu_keyboard(course_url)
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)
