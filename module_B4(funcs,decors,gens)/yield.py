def inf_decimals(step=1):
    n = 0
    yield n
    while True:
        n += step
        yield n


# for i in inf_decimals():
#    print(i)

def inf_cycle(massive):
    while True:
        cur_value = massive.pop(0)
        yield cur_value
        massive.append(cur_value)


#for i in inf_cycle([1, 2, 3, '===']):
#    print(i, end='')

# для примера возьмём строку
str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))
# Получим первый элемент строки
print(next(str_iter))  # m

# Получим ещё несколько элементов последовательности
print(next(str_iter))  # y
print(next(str_iter))  #
print(next(str_iter))  # t
print(next(str_iter))  # s
print(next(str_iter))  # t
print(next(str_iter))  #
print(next(str_iter))  #