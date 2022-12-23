# Сортировка выбором
count = 0
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)): # проходим по всему массиву

        idx_max = i # сохраняем индекс предположительно максимального элемента
        for j in range(i+1, len(array)):
                count += 1
                if array[j] > array[idx_max]:
                        idx_max = j
        if i != idx_max: # если индекс не совпадает с максимальным, меняем
                array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(f'Count = {count}')