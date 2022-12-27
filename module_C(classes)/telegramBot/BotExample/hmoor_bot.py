'''
Done! Congratulations on your new bot. You will find it at t.me/hmooryatnya_bot. You can now add
 a description, about section and profile picture for your bot, see /help for a list of commands.
  By the way, when you've finished creating your cool bot, ping our Bot Support if you want a
   better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5979517545:AAHM8S7GxDZYkaRi1Apu8YTgSXni89A2_uw
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
'''
import json

import telebot

TOKEN = '5979517545:AAHM8S7GxDZYkaRi1Apu8YTgSXni89A2_uw'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def hello_func(message):
    print(f'Получено сообщение {message}')
    print(type(message))
    bot.reply_to(message, f"{message.from_user.first_name}, привет из Хмурятни")

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.content_type == 'text' and message.text == 'Кто пиздабол?':
        bot.reply_to(message, "Майкл пиздабол")
    else:
        bot.reply_to(message, f"{message.from_user.first_name}, что тебе еще нужно?")


@bot.message_handler(content_types='photo')
def handle_photo(message):
    bot.reply_to(message, 'Nice mem xD')

bot.polling(non_stop=True)
