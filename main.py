import telebot
from telebot import types
import random

bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    markup.add(types.KeyboardButton("Рандомный напиток"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def randomize(message):
    if message.text == 'Рандомное число':
        num = random.randint(1, 100)
        bot.send_message(message.chat.id, str(num))
    if message.text == 'Рандомный напиток':
        a = ['Кофе', 'Чай','квас', 'молоко', 'сироп оп оп оп']
        bot.send_message(message.chat.id, random.choice(a))

bot.polling(none_stop=True)
