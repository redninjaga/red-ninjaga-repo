import random
import string

import telebot

# підключення до бота
bot = telebot.TeleBot('7367864457:AAEref5cyakkd-B5FNzB84u38ZsPtOrgvBg')


'''MESSAGE - словник з інформацією'''
# message.from_user
#     message.from_user.first_name
#     message.from_user.username
#     message.from_user.last_name
#
# message.chat
#     message.chat.id
#
# message.text

'''Команди'''
# bot.reply_to(message, text) - відповідає на певне повідомлення
# bot.send_message(chat_id, text) - відправляє повідомлення


# бот реагує на команди
@bot.message_handler(commands=['start', 'help'])
def get_commands(message):
    if message.text == '/start':
        bot.reply_to(message, f'Hello, {message.from_user.first_name}!')

    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Description')


# бот реагує на текстові повідмолення
@bot.message_handler(content_types=['text'])
def get_text(message):
    '''Зчитує текст повідомлення'''
    # bot.send_message(message.chat.id, f'Your text: {message.text}')

    '''Реагує на певне повідомлення'''
    # if message.text == 'python':
    #     bot.send_message(message.chat.id, 'Luck in study!')

    '''Відправляє рандомне привітання'''
    # word_welcome = ['salut', 'buna', 'witamy', 'willkommen', 'gamarjoba',
    #                 'ahoj', 'bonjour', 'hallo', 'servus', 'salom', 'hola']
    #
    # if message.text in word_welcome:
    #     bot.reply_to(message, random.choice(word_welcome))

    '''Реагує на ключові слова в повідомленням'''
    key_words = ['Python', 'Java', 'JavaScript', 'C++']
    text_user = message.text.lower().split(' ')
    text_user = [word.strip(string.punctuation) for word in text_user]

    for word in key_words:
        if word.lower() in text_user:
            bot.send_message(message.chat.id, 'This is lang programming')


# запуск бота, щоб приймав запити
bot.infinity_polling()
