def rec_f(n):
    if n > 0:
        rec_f(n-1)
    else:
        return 0
    print('n = ', n)

rec_f(5)
