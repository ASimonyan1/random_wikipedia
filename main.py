import requests
from bs4 import BeautifulSoup

goroda = ["Москва", "Беларусь", "Китай", "Япония", "Индия", "Армения", "Азербайджан", "Чечня",
          "Казахстан", "Грузия"]
for i in range(len(goroda)):
    url = f"https://ru.wikipedia.org/wiki/{goroda[i]}"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    finder = soup.find_all('p')
    if responce.status_code == 200:
        with open(f'{goroda[i]}.txt', 'w', encoding="UTF-8") as f:
            for line in finder:
                f.write(line.text)
    else:
        print(f"страница не найдена! {goroda[i]}")

import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Россия"

responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')
finder = soup.find_all('p')

with open('Russia.txt', 'w') as f:

    for line in finder:
        f.write(line.text.strip())
        f.write('\n')
