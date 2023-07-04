import requests
from random import randint
goroda = ["Москва", "Беларусь", "Китай", "Япония", "Индия", "Армения", "Азейрбарджан", "Чечня",
          "Казахстан", "Грузия"]
a = randint(0, 9)
url = f"https://ru.wikipedia.org/wiki/{goroda[a]}"
responce = requests.get(url)
print(responce.url)
