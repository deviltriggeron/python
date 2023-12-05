import telebot
from telebot import types
import random
from aiogram.types.message import ContentType

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Random number')
    item2 = types.KeyboardButton('GitHub')
    item3 = types.KeyboardButton('Game')
    keyboard.add(item1, item2, item3)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=keyboard)


@bot.message_handler()
def button(message):
    if message.text == 'Random number':
        bot.send_message(message.chat.id, 'Your number: ' + str(random.randint(0, 1000)))
    elif message.text == 'GitHub':
        markup = types.InlineKeyboardMarkup()
        web = types.InlineKeyboardButton('GitHub', url='https://github.com/deviltriggeron')
        markup.add(web)
        bot.send_message(message.chat.id, 'Visit my GitHub', reply_markup=markup)
    elif message.text == 'Game':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('RSP')
        but2 = types.KeyboardButton('Hangman')
        but3 = types.KeyboardButton('Back')
        markup2.add(but1, but2, but3)
        bot.send_message(message.chat.id, 'Select game', reply_markup=markup2)
    elif message.text == 'RSP':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Rock')
        btn2 = types.KeyboardButton('Scissors')
        btn3 = types.KeyboardButton('Paper')
        btn4 = types.KeyboardButton('Back')
        markup1.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'This is game "Rock, scissors, paper!" ', reply_markup=markup1)
    roster = ['rock', 'scissors', 'paper']
    ais = random.choice(roster)
    if message.text == 'Rock':
        bot.send_message(message.chat.id, "You select rock, i'm select " + ais)
        if ais == 'rock':
            bot.send_message(message.chat.id, 'Draw!\nTry again? or click "Back" to leave')
        elif ais == 'scissors':
            bot.send_message(message.chat.id, 'You win!\nSelect again or click "Back" to leave')
        elif ais == 'paper':
            bot.send_message(message.chat.id, 'You lose!\nTry again? or if you are scared then click "Back"')
    elif message.text == 'Scissors':
        bot.send_message(message.chat.id, "You select scissors, i'm select " + ais)
        if ais == 'rock':
            bot.send_message(message.chat.id, 'You lose!\nTry again? or if you are scared then click "Back"')
        elif ais == 'scissors':
            bot.send_message(message.chat.id, 'Draw!\nTry again? or click "Back" to leave')
        elif ais == 'paper':
            bot.send_message(message.chat.id, 'You win!\nSelect again or click "Back" to leave')
    elif message.text == 'Paper':
        bot.send_message(message.chat.id, "You select paper, i'm select " + ais)
        if ais == 'rock':
            bot.send_message(message.chat.id, 'You win!\nSelect again or click "Back" to leave')
        elif ais == 'scissors':
            bot.send_message(message.chat.id, 'You lose!\nTry again? or if you are scared then click "Back"')
        elif ais == 'paper':
            bot.send_message(message.chat.id, 'Draw\nTry again? or click "Back" to leave')
    # elif message.text == 'Hangman':
    #     WORDS = ['интернет', 'пятно', 'бизнес', 'неделя', 'червь', 'доширак']
    #     word = random.choice(WORDS)
    #     so_far = "*" * len(word)
    #     wrong = [0]
    #     used = [0]
    #     bot.send_message(message.chat.id, 'This game hangman, write letter')
    #     bot.send_photo(message.chat.id, open('hangman photo/Hangman-0.png', 'rb'))
    #     bot.send_message(message.chat.id, "Введите букву: ")
    elif message.text == 'Back':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Random number')
        item2 = types.KeyboardButton('GitHub')
        item3 = types.KeyboardButton('Game')
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Main menu', reply_markup=keyboard)


if __name__ == "__main__":
    bot.polling(none_stop=True)
