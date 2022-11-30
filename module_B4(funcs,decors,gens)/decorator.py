import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.9000f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)
N = 100
pow2_time_seq = []
inbuild_pow2_time_seq = []
for i in range(N):

    pow2_time_seq.append(pow_2())
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

    inbuild_pow2_time_seq.append(in_build_pow())
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458
print(f'Среднее время pow2: {sum(pow2_time_seq)/len(pow2_time_seq)}')
print(f'Среднее время pow2 из python: {sum(inbuild_pow2_time_seq)/len(inbuild_pow2_time_seq)}')