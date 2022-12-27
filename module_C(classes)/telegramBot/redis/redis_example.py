import json

import redis


def main():
    red = redis.Redis(
        host='redis-12098.c265.us-east-1-2.ec2.cloud.redislabs.com',
        port=12098,
        password='vyOPNI3Z4IitNtqeXjV8Ijw7YURsT27m'
    )
    dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
    #red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
    converted_dict = json.loads(
        red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
    print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
    print(converted_dict)
    red.delete('dict1')  # удаляются ключи с помощью метода .delete()
    print(red.get('dict1'))


if __name__ == '__main__':
    main()
