def do_it_twice(func):
    def wrapper(*args, **kwargs):
        print('Блок кода обертки до двойного вызова целевой функции')
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('Блок кода обертки после двойного вызова целевой функции')

    return wrapper


@do_it_twice
def say_word(*args, **kwargs):
    print(f'ПОзиционные аргументы:')
    for arg in args:
        print(f'{arg}', end='   ---   ')
    print('')
    print(f'Именованные аргументы:')
    for key,value in kwargs.items():
         print(f'{key} = {value}')

    #print(type(kwargs))
    #for arg in kwargs:
    #    print(type(arg))
    #    print(arg)
    #    print(kwargs[arg])


say_word("Oo!!!", "Второй аргумент", name="Иван", age=25)
