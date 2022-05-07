import telebot
import sys


token = '5349684609:AAE7SJYilWL1h-75ojIpMK0DTeBjYO6YS1k'
bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Я на связи. Напиши мне что-нибудь)')
    
    
    @bot.message_handler(commands = ['help'])
    def help(message):
        bot.send_message(message.chat.id, 'Я умею: пока ничего')


    @bot.message_handler(commands=['time'])
    def time(message):
        bot.send_message(message.chat.id, 'Напиши чёнить:')
        @bot.message_handler()
        def echo(m):
            bot.send_message(m.chat.id, f'Вы написали "{m.text}"')
            
        bot.polling(none_stop=True)
        
        @bot.message_handler(commands=['stop'])
        def stop(message):
            bot.send_message(message.chat.id, 'Пока-пока')
            sys.exit()
            
        bot.polling(none_stop=True)


bot.polling(none_stop=True)