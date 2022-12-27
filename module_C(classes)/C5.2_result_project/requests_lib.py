import json

import requests

'''
r = requests.get(
    'https://baconipsum.com/api/?type=meat-and-filler')  # делаем запрос на сервер по переданному адресу
print(r.content)
texts = json.loads(r.content)
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль, оставим только первые 50 символов.
    print(text[:50], '\n')

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
print('======= JSON ===========')
print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

r = requests.post('https://httpbin.org/post', data={'my key': 'my value'})  # отправляем POST-запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с GET-запросами, разницы никакой нет
'''
data = {'key2': 'value2'}

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=json')  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)
texts = json.loads(r.content)
print(type(texts))
print("first text (texts[0]):", texts[0])
