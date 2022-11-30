def zero_check(func):
    def wrapper(a):
        if not a:
            return f'Ошибка! Нельзя делить на {a}'
        else:
            return func(a)

    return wrapper


def rounder(func):
    def wrapper(a, round_count=3):
        #print('arg = ', a, 'f(a) = ', func(a))
        return round(func(a), round_count)

    return wrapper


@zero_check
@rounder
def inverse(a):
    return 1 / a


print(inverse(3))
print(inverse(0))
print('THE END')
