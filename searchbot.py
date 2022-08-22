from youtubesearchpython import *
import telebot


def SearchYou(title):
    customSearch = CustomSearch(title, VideoSortOrder.uploadDate)
    s = []
    for i in range(3):
        s.append(i)
        s.append(customSearch.result()['result'][i]['link'])
        s.append(customSearch.result()['result'][i]['title'])
        s.append(customSearch.result()['result'][i]['channel']['name'])
    return s

# Создаем экземпляр бота
bot = telebot.TeleBot('5583093814:AAFDif3zAy6KhYDGDET5XbaMBu-_y9-DHTo')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напиши мне название книги )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # log
    f = open('A:\YoutubeSearch\data' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    f.write('u: ' + message.text + '\n')
    f.close()
    #
    customSearch = CustomSearch(message.text, VideoSortOrder.uploadDate)
    s = []
    for i in range(3):
        s.append(i)
        s.append(customSearch.result()['result'][i]['link'])
        s.append(customSearch.result()['result'][i]['title'])
        s.append(customSearch.result()['result'][i]['channel']['name'])
    answer = s


    f = open('A:\YoutubeSearch\data332381885_log.txt', "rb")
    bot.send_document(message.chat.id, f)
# Запускаем бота
bot.polling(none_stop=True, interval=0)


