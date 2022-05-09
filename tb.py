import telebot
from Video import Video
import pickle

with open("coded_list.pkl", "rb") as fp:
    vid_list = pickle.load(fp)


token = '5349684609:AAE7SJYilWL1h-75ojIpMK0DTeBjYO6YS1k'
bot = telebot.TeleBot(token)
flag = False

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Я на связи. Я бот лектория ФБМФ. Для поиска кода напишите команду /getvideo')
    
    
    @bot.message_handler(commands = ['help'])
    def help(message):
        bot.send_message(message.chat.id, 'Для поиска видео напиши мне команду /getvideo , после чего напиши тему, которую хотелось бы разобрать. Я пришлю тебе все видеоролики, в котором была затронута данная тема с таймкодами, чтобы было удобнее готовиться. Удачи)')


    @bot.message_handler(commands=['getvideo'])
    def getvideo(message):
        bot.send_message(message.chat.id, 'Напиши тему:')
        @bot.message_handler()
        def search(message):
            si = message.text
            for i in vid_list:
                if si in i.desc:
                    bot.send_message(message.chat.id, f'{i.name}\n\n{i.url}\n\n{i.desc}')
     
bot.polling(none_stop=True)
