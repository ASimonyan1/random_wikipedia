import time
import requests
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
import PySimpleGUI as sg
dates = ["yesterday", "today", "tomorrow", "week", "month", "year"]
zodiaks = ["aries", "leo", "sagittarius", "taurus", "virgo", "capricorn", "gemini", "libra", "aquarius", "cancer", "scorpio", "pisces"]
bar = IncrementalBar('Countdown', max = len(dates) * len(zodiaks))
j = 0
for i in range(len(dates)):
    for u in range(len(zodiaks)):
        url = f"https://horo.mail.ru/prediction/{zodiaks[u]}/{dates[i]}/"
        responce = requests.get(url)
        while responce.status_code != 200:
            time.sleep(0.5)
            responce = requests.get(url="https://horo.mail.ru/prediction/" + zodiaks[u] + '/' + dates[i] + '/')
        soup = BeautifulSoup(responce.text, 'lxml')
        info = soup.find_all('p')
        text_zodiak = info[0].text + '\n' + info[1].text
        with open(f'Files/{zodiaks[u]}-{dates[i]}.txt', 'w', encoding="UTF-8") as f:
            f.write(text_zodiak)
        sg.one_line_progress_meter('This is my progress meter!', j+1,  len(dates) * len(zodiaks), '-key-')
        j += 1
bar.finish()



# создать для каждого знака файл на каждую дату(72 файла)