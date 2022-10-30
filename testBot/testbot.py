import telebot
from telebot import types
import random
TOKEN = '5451283068:AAF9J6CVNsy8W4WY9vovaGbKWYuowh4M0j0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Random number')
    item2 = types.InlineKeyboardButton('My GitHub', url="https://https://github.com/deviltriggeron")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, (f'Hello {message.from_user.first_name}'), reply_markup = markup)

@bot.message_handler()
def button(message):
    if message.text == 'Random number':
        bot.send_message(message.chat.id, 'Your number: ' + str(random.randint(0, 1000)))
    elif message.text == 'My GitHub':
        bot.send_message(message.chat.id, "Visit my GitHub: ")


if __name__ == '__main__':
    bot.polling(none_stop = True)