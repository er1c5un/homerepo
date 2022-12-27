import redis


def console(redis=None):
    while True:
        cmd = input("Введите имя контакта или команду:").split()
        if len(cmd) > 1:
            key = cmd[1]
            if len(cmd) == 3:
                value = cmd[2]
            else:
                value = None
            if cmd[0] == 'set':
                redis.set(key, value)
                print(f'Запись {key} сохранена')
            elif cmd[0] == 'del':
                redis.delete(key)
                print(f'Запись {key} удалена')
        else:
            print(redis.get(cmd[0]))

def main():
    red = redis.Redis(
        host='redis-12098.c265.us-east-1-2.ec2.cloud.redislabs.com',
        port=12098,
        password='vyOPNI3Z4IitNtqeXjV8Ijw7YURsT27m'
    )
    console(red)


if __name__ == '__main__':
    main()
