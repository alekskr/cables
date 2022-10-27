import requests
from bs4 import BeautifulSoup
import json
import os
import random
from time import sleep
import pandas as pd


url = 'https://bystrokabel.ru/item/mpo'
# В метод get() вторым параметром передадим заголовки. В заголовки добавим accept и user agent. Делается для того, +\
# чтобы показать сайту, что мы не бот. Правой кнопкой мыши - просмотреть код - во вкладке Network в любом из +\
# get-запросов Headers - Requests Headers:

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# req = requests.get(url, headers=headers)

# Теперь сохраним страницу в файл:
# src = BeautifulSoup(req.content, 'html.parser').prettify()
# with open('provoda_mpo.html', 'w', encoding='UTF-8') as file:
#     file.write(src)

# Код запроса и код сохранения больше не нужны и можно их закомментировать.
# Далее откроем файл, прочитаем и сохраним код страницы в переменную:
# with open('provoda_mpo.html', 'r', encoding='UTF-8') as file:
#     src = file.read()
# print(src)

# Создадим объект soup, передадим переменную src и парсер:
# soup = BeautifulSoup(src, 'html.parser')

# all_cable_diameters_dict = {}
# all_cable_diameters = soup.find(class_='table-remains').find_all('a')
# print(all_cable_diameters)
# for j in all_cable_diameters:
#     item_text = j.text.strip()
#     item_link = 'https://bystrokabel.ru' + str(j.get('href'))
#     all_cable_diameters_dict[item_text] = item_link
# print(all_cable_diameters_dict)

# Сохраним словарь с ссылками в json-файл:
# with open('provoda_mpo_urls.json', 'w', encoding='UTF-8') as file:
#     json.dump(all_cable_diameters_dict, file, indent=4, ensure_ascii=False)

# Теперь можно закомментировать весь код выше и загрузим json-файл в переменную:
# with open('provoda_mpo_urls.json', encoding='UTF-8') as file:
#     all_cable_types = json.load(file)
# print(all_cable_types)

# Теперь нужно создать цикл, на каждой итерации которого мы будем заходить на новую страницу типа провода и собирать +\
# там информацию и записывать в файл. Каждую страницу сохранять под именем типа провода. Все пробелы в наименованиях +\
# типов провода заменим на нижнее подчеркивание. Переменная count на данном этапе нужна, чтобы для начала поработать +\
# с одной страницей, а не бомбить сайт запросами.
# # count = 0
# for cable_name, cable_link in all_cable_types.items():
#     # if count == 0:
#     if ' ' in cable_name:
#         cable_name = cable_name.replace(' ', '_')
#
#     req = requests.get(url=cable_link, headers=headers)
#     src = req.text
#
#     with open(f'data_provoda_mpo\\{cable_name}.html', 'w', encoding='UTF-8') as file:
#         file.write(src)
#
#             # count += 1
# Далее count можно убрать, сохранить все страницы в файлы и закомментировать эту часть кода.

# Код выше можно закомментировать. Теперь открываем json-файл и циклом переходим по каждой ссылке. В открывшейся +\
# странице ищем код ссылки на страницу с информацией. И каждую страницу с информацией сохраняем в html-файл для +\
# дальнейшего сбора информации о конкретном проводе.

with open('provoda_mpo_urls.json', encoding='UTF-8') as file:
    all_cable_diameters = json.load(file)

# count - счетчик пройденных ссылок.
# try - попытаться найти нужные данные о проводе.
# if - условие, если при переходе на страницу с указанным диаметром нет данных по проводу, но есть еще ссылки на +\
# страницу с информацией. Ищем класс class_='info noborder' и в нем ссылку на страницу с данными.
# elif - условие, если при переходе на страницу с указанным диаметром есть все данные. Ищем класс class_='mark-name' .
# file name - имя файла в виде заголовка страницы .h1.text. file_name[7:] - это нужно, чтобы из имени файла +\
# исключить слово “провод”.
# sleep - остановка программы на 1-3 секунды, чтобы не бомбить сервер.
# except - данных о проводе нет.

# count = 0
# print(f'Всего итераций {len(all_cable_diameters)}')
# spisok_proverennyh_ssylok = []
# for cable_name_diameter, cable_link in all_cable_diameters.items():
#     if cable_link not in spisok_proverennyh_ssylok:
#         req = requests.get(cable_link, headers=headers)
#         soup = BeautifulSoup(req.content, 'html.parser')
#         count += 1
#
#         try:
#             print(f'# Итерация {count}')
#             info_link = 'https://bystrokabel.ru' + soup.find(class_='info noborder').get('href')
#             print('info link= ', info_link)
#             req2 = requests.get(info_link, headers=headers)
#             file_name = BeautifulSoup(req2.content, 'html.parser').h1.text
#             print('file name= ', file_name[7:])
#             with open(f'all_diameters_provoda_mpo\\{file_name[7:]}.html', 'w', encoding='UTF-8') as file:
#                 file.write(req2.text)
#             print(f'# Итерация {count}. Файл записан!')
#             sleep(random.randrange(2, 4))
#
#         except (TypeError, AttributeError):
#             print(f'#Ошибка. Итерация {count}. {cable_name_diameter} не записан...')
#             sleep(4)
#     spisok_proverennyh_ssylok.append(cable_link)


# После того, как все html-файлы готовы, можно приступать к извлечению данных из них.
# При парсинге могут образовываться неопнятные символы, например символы от возведения в степень. Создаем список +\
# кортежей, где первый элемент кортежа символ, а второй то, на что его заменить.


def formatting(fraze):  # функция замены непонятных символов
    """Removes wrong symbols."""
    formatting_list = [
        ('\xa0', ' ')]
    for q in formatting_list:
        fraze = fraze.replace(q[0], q[1])
    return fraze


all_cables = []  # список всех кабелей
# Создаем список html-файлов:
all_files_cable_diameters = os.listdir('all_diameters_provoda_mpo')
# print(all_files_cable_diameters)

# По очереди открываем все файлы и ищем нужную информацию:
for i in all_files_cable_diameters:
    file_name = 'all_diameters_provoda_mpo\\' + i
    with open(file_name, 'r', encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'html.parser')
    print(soup.h1.text[7:])

    # Определение типа провода и создание словаря характеристик провода:
    cable_properties = {'Провод': soup.h1.text[7:]}  # [7:] означает, что из заголовка страницы убираем слово "Провод".

    # Определение ссылки провода из файла all_cable_type_dict.json:
    for cable_name_diameter, cable_link in all_cable_diameters.items():
        if cable_name_diameter == cable_properties['Провод']:
            cable_properties['Ссылка'] = cable_link

    # парсинг расшифровки провода
    decoding_1 = soup.find_all(class_="letters")  # ищем все символы в обозначении провода
    decoding_1_list = []
    for letter in decoding_1:
        decoding_1_list.append(letter.text)
    # print(decoding_1_list)

    decoding_2 = soup.find(class_="item-decode-description").text.strip()  # описание символов в обозначении
    decoding_2_list = formatting(decoding_2).split('\n')
    # print(decoding_2_list)

    decoding = ''  # создаем строку, содержащую и символы, и их описание
    for index in range(len(decoding_1_list)):
        if len(decoding_1_list) == len(decoding_2_list):
            decoding += decoding_1_list[index] + ': ' + decoding_2_list[index] + '  '
        else:
            try:
                decoding += decoding_2_list[index] + '  '
            except IndexError:  # на случай, если описание неполное
                continue
    # print('decoding', decoding)

    cable_properties['Расшифровка'] = decoding

    # список параметров, которые запишем в таблицу excel:
    required_parameters = ['Наружный диаметр',
                           'Минимальный радиус изгиба',
                           'Диапазон рабочих температур']

    param_names = soup.find_all(class_='param-name')  # поиск названий параметров
    param_values = soup.find_all(class_='param-value')  # поиск значений параметров
    param_names_list = [i.text for i in param_names]
    param_values_list = [i.text for i in param_values]

    all_name_value = dict(zip(param_names_list, param_values_list))
    # print('all_name_value', all_name_value)

    # проверка на соответствие нужному списку параметров required_parameters:
    name_value = {}
    for k, v in all_name_value.items():
        if k in required_parameters:
            name_value[k] = v
    # print('name_value', name_value)

    cable_properties.update(name_value)  # добавляем нужные параметры в словарь параметров провода
    all_cables.append(cable_properties)  # данный провод добавляем в список всех проводов
    # print(cable_properties)

# print(all_cables)

# создание Data Frame
# создаем заголовки таблицы
data = pd.DataFrame({'Провод': [],
                     'Наружный диаметр': [],
                     'Минимальный радиус изгиба': [],
                     'Диапазон рабочих температур': [],
                     'Ссылка': [],
                     'Расшифровка': []})

# добавление в таблицу всех проводов
for i in all_cables:
    i_frame = pd.DataFrame([i])
    data = pd.concat([data, i_frame], ignore_index=True)

# сохраняем в csv-файл
data.to_csv('data\\provoda_mpo.csv', index=False, encoding='utf-8')
