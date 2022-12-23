num_array_1 = [2, 3, 1, 4, 6, 5, 9, 8, 7]
num_array_2 = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def insertion_sort(array):
    cnt = 0
    for i in range(1, len(array)):
        x = array[i]
        index = i
        while index > 0 and array[index - 1] > x:
            cnt += 1
            array[index] = array[index - 1]
            index -= 1
        array[index] = x
    print(f'Количество сравнений в моем варианте: {cnt}')


def insertion_sort_example(array):
    count = 0
    for i in range(1, len(array)):
        x = array[i]
        print('Ведущий элемент', x)
        print('Индекс', i)
        idx = i
        while idx > 0:
            count += 1
            print(f'Делаем сравнение №{count}')
            if array[idx-1] <= x:
                print(f'{array[idx-1]} <= {x}, переставлять не нужно')
                break
            print(f'{array[idx-1]} > {x}, сдвигаем')
            array[idx] = array[idx-1]
            idx -= 1
            print(f'Теперь индекс {idx}')
        array[idx] = x
        print(f'{x} вставлен на место. Массив {array}')
    print(f'Количество сравнений в их варианте: {count}')

print('Мой вариант')
print(num_array_1)
insertion_sort(num_array_1)
print(num_array_1)
print('-' * 30)
print('Их вариант')
print(num_array_2)
insertion_sort_example(num_array_2)
print(num_array_2)
print('-' * 30)
