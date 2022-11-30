L = ['THIS', 'IS', 'LOWER', 'STRING']
l = list(map(str.lower, L))
print(l)

some_list = [-2, -1, 0, 1, -3, 2, -3]

def chet(x):
    return x % 2 == 0

result = filter(chet, some_list)
print(list(result))