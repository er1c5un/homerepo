'''
В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за
контрольную. Выведите на экран всех учащихся, чья оценка меньше 3 баллов. Cодержание файла:
'''

file = 'results.txt'

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        if line[-2].isdigit() and int(line[-2]) < 3:
            print(' '.join(line.split()[:2]))

#with open(file, 'r', encoding='utf-8') as file:
#    for line in file:
#        points = int(line.split()[-1])
#        if points < 3:
#            name = " ".join(line.split()[:-1])
#            print(name)
