try:
    a = int(input())
except ValueError:
    print("Вы ввели неправильное число")
else:
    print("Вы ввели правильно число")
finally:
    print("Выход из программы")