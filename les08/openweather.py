# coding=utf-8
"""
== OpenWeatherMap ==
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.
Необходимо решить следующие задачи:
== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)
        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up
        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in
        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a
    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}
== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):
    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных
2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))
3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.
При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.
При работе с XML-файлами:
Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>
Чтобы работать с пространствами имен удобно пользоваться такими функциями:
    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''
    tree = ET.parse(f)
    root = tree.getroot()
    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}
    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...
"""
import json
import requests
import sys
import sqlite3
import os
import datetime

non_city = True
answer = ''
country_lst = []
info = {}
city_ = ''
today = datetime.datetime.now()

with open('city.list.json', 'r', encoding='UTF-8') as city:
    city_string = city.read()

with open('city.list.json', 'r', encoding='UTF-8') as city:
    city_dict = json.loads(city.read())

with open('app.id', 'r', encoding='UTF-8') as id:
    app_id = id.readline()[1:]

# запрос у пользователя города и страны или ID города
while non_city == True:
    answer = input('Если вы знаете город и страну - нажмите "+", если знаете ID - нажмите "-", чтобы выйти - "0": ')
    if answer == '+':
        while non_city == True:
            print('Введите Q, если хотите выйти или введите город и страну: ')
            city_ = input('city: ').title()
            if city_.upper() == 'Q':
                sys.exit(0)
            country_ = input('country: ').upper()
            try:
                for item in city_dict:
                    if item['name'] == city_ and item['country'] == country_:
                        city_id = item['id']
                        non_city = False
                if non_city == False:
                    break
                else:
                    print(f'Города {city_} нет в стране {country_}')
            except Exception as e:
                print(e)
    elif answer == '-':
        city_id = int(input('Введите id города: '))
        non_city = False
    elif answer == '0':
        sys.exit(0)
    else:
        print('Вы ввели что-то не то!')
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'type': 'like', 'units': 'metric', 'APPID': app_id})
    info = res.json()
    print(f"city: {info['name']}")
    print(f"country: {info['sys']['country']}")
    print(f"conditions: {info['weather'][0]['description']}")
    print(f"temp: {info['main']['temp']}")
    print(f"temp_min: {info['main']['temp_min']}")
    print(f"temp_max: {info['main']['temp_max']}")
    print(f"today: {today.strftime('%d-%m-%Y')}")
except Exception as e:
    print("Exception (find):", e)
# Создаем файл БД
name_db = 'weather.db'
cur_dir = os.getcwd()
path_db = os.path.join(cur_dir, name_db)
if not os.path.exists(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    try:
        # создание таблиц + наполнение
        cursor.execute("""CREATE TABLE 'weather'
                          (id_city integer PRIMARY KEY, name_city varchar(255), date date,
                           temperature integer, id_weather integer);
                       """)
        cursor.execute("""INSERT INTO weather
        (id_city, name_city, date, temperature, id_weather) VALUES (?, ?, ?, ?, ?)""",
                       (info['id'], info['name'], today.strftime('%d-%m-%Y'), info['main']['temp'], info['weather'][0]['id']))
        conn.commit()
        print('База данных успешно создана')
    except sqlite3.Error as e:
        print(f'Ошибка БД: {e}')
else:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if os.path.isfile('weather.db'):
        cursor.execute("""INSERT OR REPLACE INTO 'weather' 
        (id_city, name_city, date, temperature, id_weather) VALUES (?, ?, ?, ?, ?)""",
                       (info['id'], info['name'], today.strftime('%d-%m-%Y'), info['main']['temp'], info['weather'][0]['id']))
        conn.commit()
        cursor.close()
        conn.close()
        print('База данных обновлена')
