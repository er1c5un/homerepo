#aaabbccccdaa
txt = input()
result = ''
last = txt[0]
count = 0
for s in txt:
    if s == last:
        count += 1
    else:
        result += last + str(count)
        count = 1
    last = s
result += last + str(count)
print('RESULT = ', result)
