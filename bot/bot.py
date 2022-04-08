import requests
import telebot
import json
import traceback
from config import Convertor

class APIException(Exception):
    pass

TOKEN = ''
exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = "Привет, решил поднять на валюте?\n" \
           "_______________________________\n" \
           "Это надобыло делать 8 лет назад\n" \
           "_______________________________\n" \
           "Ладно введи валюту для перевода\n" \
           "_______________________________\n" \
           "Пример: 10 евро рубль\n" \
           "_______________________________\n" \
           "Список валют команда /values"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def start(message: telebot.types.Message):
    text = "Тебе уже ничего не поможет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

# @bot.message_handler(content_types=['text'])
# def hi(message: telebot.types.Message):
#     hi = message.text.lower()
#     if hi == 'привет':
#         bot.send_message(message.chat.id, ' \
#         Какой привет. нажми на команду /start')
#     else:
#         converter(hi)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    value = message.text.split(' ')
    print(value)
    try:
        if len(value) != 3:
            raise APIException('Неверное количество параметров!')
        else:
            print(value)
            answer = Convertor.get_price(value)
            # print(answer)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)













bot.polling(none_stop=True)


# c = Convertor()
# print(c.get_price(['10', 'евро', 'доллар']))
