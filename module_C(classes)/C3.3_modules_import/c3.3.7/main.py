from module import square_square, circle_square

circle_r = int(input("Введите радиус круга:"))
a, b = input("Введите стороны прямоугольника через пробел:").split()
a = int(a)
b = int(b)
s_circle = circle_square(circle_r)
s_rect = square_square(a, b)
print("Площадь круга", s_circle)
print("Площадь прямоугольника", s_rect)
if s_circle > s_rect:
    print("Площадь круга больше")
else:
    print("Площадь прямоугольника больше")
