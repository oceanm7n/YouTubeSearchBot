
from youtubesearchpython import *


def SearchYou(title):
   try:
        customSearch = CustomSearch(title, VideoSortOrder.uploadDate)
        s = []
        for i in range(5):
            print('ТЕКСТ ЗАПРОСА:', title, '\n')
            print(str(i)+'.' ,'Название канала:', customSearch.result()['result'][i]['channel']['name'])
            print('Ссылка:',customSearch.result()['result'][i]['link'], '\n' )
            print('Название:',customSearch.result()['result'][i]['title'], '\n')
   except IndexError:
       print("Не найдено более 1 ссылки")


with open("A:\YoutubeSearch\qwe.txt") as file:
    titles = file.readlines()
    for i, title in enumerate(titles):
        titles[i]= title[:-1]
        SearchYou(titles[i])



