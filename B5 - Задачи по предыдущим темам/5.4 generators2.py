USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


def has_access(func):
    def wrapper():
        if username in USERS:
            print('Доступ разрешен')
            func()
        else:
            print('Доступ запрещен')
    return wrapper


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")

    return wrapper


@is_auth
@has_access
def from_db():
    print("some data from database")


from_db()
