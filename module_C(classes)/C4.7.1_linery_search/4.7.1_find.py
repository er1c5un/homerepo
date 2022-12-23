#  функция подсчета количества вхождений эл-та в массиве
def count(array, element):
    cnt = 0
    for el in array:
        if el == element:
            cnt += 1
    return cnt


#  функция двоичного поиска (принцип разделяй и влавствуй)
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит, элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))