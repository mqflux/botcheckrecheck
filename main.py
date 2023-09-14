import telebot
import random
import os


rm_img = ["https://cdn.britannica.com/25/172925-050-DC7E2298/black-cat-back.jpg",
          ]


bot = telebot.TeleBot("6276727396:AAHAbJRKugcBL8pVI5gsyMpbSvFOSLlaP3A")


@bot.message_handler(content_types=['text'])
def on_get_message(message):
    if message.text == "/random_image":
        send_random_image(message.chat.id)
    elif message.text == "/random_sound":
        pass


def send_random_image(chat_id):
    bot.send_photo(chat_id, "https://cdn.britannica.com/25/172925-050-DC7E2298/black-cat-back.jpg")


def send_random_audio():
    pass


def get_random_file(path):
    return random.choice(os.listdir(path))


bot.polling(none_stop=True, interval=0)


