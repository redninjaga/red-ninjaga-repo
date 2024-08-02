import telebot
from telebot import types  # для створення клавіатур

bot = telebot.TeleBot('7227984936:AAEXL3CfZn9PVGO1_uYI6UC3RNQNRpWq9gA')

'''Reply keyboard (підекранна клавіатура)'''

#створення клавіатури
reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  #resize_keyboard - робить кнопки нормального розміру

#створення кнопок
bt1 = types.KeyboardButton('Button1')
bt2 = types.KeyboardButton('Button2')
bt3 = types.KeyboardButton('Button3')

#додаємо кнопки в клавіатури
reply_keyboard.add(bt1, bt2)
reply_keyboard.add(bt3)


'''Inline keyboard (клавіатура серед повідомлень)'''

#створення клавіатури
inline_keyboard = types.InlineKeyboardMarkup()

#створення кнопок (callback_data - дані, які будуть відправлятися боту)
bt1 = types.InlineKeyboardButton('Button1', callback_data='1')
bt2 = types.InlineKeyboardButton('Button2', callback_data='😎')
bt3 = types.InlineKeyboardButton('Button3', callback_data='2024')

#додаємо кнопки в клавіатури
inline_keyboard.add(bt1, bt2, bt3)


@bot.message_handler(commands=['start', 'get_reply_kb', 'get_inline_kb'])
def get_commands(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, f'Commands:\n'
                                          f'/get_reply_kb\n'
                                          f'/get_inline_kb')

    elif message.text == '/get_reply_kb':
        #reply_markup - вказуємо клавіатуру, яку хочемо надати
        bot.send_message(message.chat.id, 'Get reply kb', reply_markup=reply_keyboard)

    elif message.text == '/get_inline_kb':
        bot.send_message(message.chat.id, 'Get inline kb', reply_markup=inline_keyboard)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Button1':
        bot.send_message(message.chat.id, 'Click button1')

    elif message.text == 'Button2':
        reply_keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reply_keyboard2.add('Button😍', 'Button😐')

        bot.send_message(message.chat.id, f'Click button2', reply_markup=reply_keyboard2)

    elif message.text == 'Button😍':
        bot.reply_to(message, 'Love')


#обробник зворотніх запитів (даних)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call.data)  # зворотні дані, які були відправлені

    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Click button1')

    if call.data == '😎':
        keyboard = types.InlineKeyboardMarkup()

        #КНОПКА З ПОСИЛАНННЯМ
        button = types.InlineKeyboardButton('ItHillel', url='https://ithillel.ua/')
        keyboard.add(button)

        bot.send_message(call.message.chat.id, 'GO', reply_markup=keyboard)


bot.infinity_polling()

