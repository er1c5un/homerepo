def find_min_recursive(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < find_min_recursive(L[1:]) else find_min_recursive(L[1:])

def mirror2(dec):
    str_dec = list(str(dec))
    if len(str_dec) >= 2:
        str_dec[0], str_dec[-1] = str_dec[-1], str_dec[0]
        mirror(str_dec[1, -1])

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

result = mirror(12345)
print(result)