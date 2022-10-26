API_KEY = ''


import telebot
from main import Coinmarketcap
c = Coinmarketcap()

def telegram_bot(API):
    bot = telebot.TeleBot(API)

    @bot.message_handler(commands=['mars_dao'])
    def send_message(messega):
        bot.send_message(messega.chat.id, c.get_all_token())

    bot.polling()    


telegram_bot(API_KEY)