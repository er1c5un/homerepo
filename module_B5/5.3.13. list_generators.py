#mul_table = [[i*j for j in range(1, 11)] for i in range(1, 11)]
#for str in mul_table:
#    print(str)

L = [int(input()) % 2 == 0 for i in range(5)]
print(not all(L) and any(L))