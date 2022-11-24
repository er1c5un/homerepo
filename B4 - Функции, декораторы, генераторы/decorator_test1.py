def my_decorator(fn):
    cache = {}

    def wrapper(*args, **kwargs):
        nonlocal cache
        if args[0] not in cache:
            cache[args[0]] = fn(*args, **kwargs)
        else:
            print(f'Берем из Кеша')
        return cache[args[0]]
    return wrapper


@my_decorator
def f(n):
    return n * 10

print(f(1))
print(f(3))
print(f(5))
print(f(3))
print(f(5))

