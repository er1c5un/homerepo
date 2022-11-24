#for a, b in zip([i for i in range(10)], [i for i in range(10, 0, -1)]):
#    print(f'{a} * {b} =', a * b)
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M =[i for i in range(10, 0, -1)]
# 10 9 8 7 6 5 4 3 2 1
# список с поэлементным произведением двух списков
result = [a * b for a, b in zip(L, M)]
print(result)
