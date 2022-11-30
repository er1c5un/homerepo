# (вес, рост)
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]

#data_index = list(map(lambda x: x[0] / (x[1] ** 2), data))
#print(data_index)
print(data)
print(sorted(data, key=lambda x: x[0] / (x[1] * 100) ** 2))
# сортировка списка по индексу массы (в качестве ключа передается функция)

a = ["asd", "bbd", "ddfa", "mcsa"]

print(*list(map(len, a)))
print(*list(map(lambda x: len(x), a)))

