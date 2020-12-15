from audioop import add

import telebot

bot = telebot.TeleBot('1463135558:AAFEe7HnmoDqa1rCnjlvoAxq2q_FZk1pwIs')
keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('посоветуй фильм','алиса или сири','я тебя люблю','bmw или мерс','arman или tolebi','алматы или астана' )


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,я сэнсэй бот.Дам советы в любой теме  ' ,reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'посоветуй фильм':
        bot.send_message(message.chat.id, 'А ты смотрел Дэдпул угарный фильм поглянь браток ')
    elif message.text.lower() == 'алиса или сири':
        bot.send_message(message.chat.id, 'мне нравиться Алиса,кстати мы сней мутим XD)')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'bmw или мерс':
        bot.send_message(message.chat.id, 'хорошую тачку в трех буквах не назовешь дурачок!')
    elif message.text.lower() == 'arman или tolebi':
        bot.send_message(message.chat.id, 'хорошую мужик в пят буквах не назовешь дурачок!')
    elif message.text.lower() == 'алматы или астана':
        bot.send_message(message.chat.id, 'мне нравиться алматы)')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()