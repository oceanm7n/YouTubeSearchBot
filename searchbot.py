from youtubesearchpython import *
import telebot


def SearchYou(title):
    try:
        customSearch = CustomSearch(title, VideoSortOrder.uploadDate)
        
        messages = []
        for i in range(5):
            channel_name = customSearch.result()['result'][i]['channel']['name']
            link = customSearch.result()['result'][i]['link']
            link_title = customSearch.result()['result'][i]['title']

            res = ''
            res += f'ТЕКСТ ЗАПРОСА:\n{title}\n\n'
            res += f'Название канала:\n{channel_name}\n\n'
            res += f'Ссылка:\n{link}\n\n'
            res += f'Название:\n{link_title}\n\n'
            res += f'Порядковый номер: {i}'
            messages.append(res)

    except IndexError:
        return "Ничего не найдено"

    return messages

def extract_arg(arg):
    return arg

# Создаем экземпляр бота
with open('key') as a:
    key = a.readlines()[0]
    bot = telebot.TeleBot(key)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    print(f'Message received from {message.from_user}')
    print(f'Text: {message.text}')
    bot.send_message(message.chat.id, 'Напиши мне название книги )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(f'Message received from {message.from_user}')
    print(f'Text: {message.text}')
    args = extract_arg(message.text)
    if args:
        res = SearchYou(args)
        for i in res:
            bot.send_message(message.chat.id,  i)

# Запускаем бота
bot.polling(none_stop=True, interval=0)


