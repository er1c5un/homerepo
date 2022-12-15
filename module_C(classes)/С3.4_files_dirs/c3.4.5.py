num_list = []
with open('numbers.txt', 'r') as f:
    for line in f:
        num_list.append(int(line))
max = max(num_list)
min = min(num_list)
sum = max + min

with open('numbers_output.txt', 'w') as f:
    f.write('Сумма наибольшего и наименьшего значения из файла numbers.txt = ' + str(sum))
