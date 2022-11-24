a = int(input())
#if 100 <= a <= 999 and not (a % 2 or a % 3):
#    print('YES')
#else:
#    print('NO')

if all([100 <= a <= 999,
        not (a % 2 or a % 3)]):
    print('YES')
else:
    print('NO')