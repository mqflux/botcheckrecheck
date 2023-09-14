import telebot
from telebot import types
import random
import os


rm_img = ["https://github.com/mqflux/botcheckrecheck/blob/master/static/random_image/black-cat-back.png",
          "https://github.com/mqflux/botcheckrecheck/blob/master/static/random_image/cat1.png"]


rm_snd = ["https://github.com/mqflux/botcheckrecheck/blob/master/static/random_sound/Pleasant_bling.mp3",
          "https://github.com/mqflux/botcheckrecheck/blob/master/static/random_sound/opa.audio.mp3"]


bot = telebot.TeleBot("6276727396:AAHAbJRKugcBL8pVI5gsyMpbSvFOSLlaP3A")


@bot.message_handler(content_types=['text'])
def on_get_message(message):
    if message.text == "/random_image":
        send_random_image(message.chat.id)
    elif message.text == "/random_sound":
        send_random_audio(message.chat.id)
    elif message.text == "/help":
        markup = types.ReplyKeyboardMarkup(row_width=2)

        itembtn1 = types.BotCommand("/random_image")
        itembtn2 = types.KeyboardButton('v')
        itembtn3 = types.KeyboardButton('d')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


def send_random_image(chat_id):
    bot.send_photo(chat_id, random.choice(rm_img))


def send_random_audio(chat_id):
    bot.send_audio(chat_id, random.choice(rm_snd))


def get_random_file(path):
    return random.choice(os.listdir(path))


bot.polling(none_stop=True, interval=0)


