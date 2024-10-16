import requests
from PIL import Image
import pandas


# Работа с requests

r1 = requests.get('https://www.sravni.ru/ege-oge/info/russkij-yazyk-padezhi-v-russkom-yazyke/')
r2 = requests.get('https://images.uzum.uz/cphuopu0t1llbtq5vcv0/original.jpg', stream=True)
with open('Bat.jpg', 'wb') as file:
    file.write(r2.content)
print(r1)


# Работа с pandas + requests

df = pandas.read_html(r1.content, match='ВСПОМОГАТЕЛЬНОЕ СЛОВО')
print(df)
print()
for i in df:
    df1 = i
df1.to_json('table.json')
df1.drop(axis=0, index=[5, 6], inplace=True)
print(df1)


# Работа с pillow

with Image.open('Bat.jpg') as img:
    img.resize((800, 600)).save('new_bat_size.png')
    img.convert("L").save('new_bat_color.png')
