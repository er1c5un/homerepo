'''lst = []
with open('results.txt', encoding='utf-8') as f:
    for line in f:
        lst.append(line)
lst = lst[::-1]
with open('result_reverse.txt', 'w') as f:
    f.writelines(lst)'''

with open('results.txt', 'r') as input_file:
   with open('result_reverse.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)

