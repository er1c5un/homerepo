class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException("Сторона квадрата не может быть меньше 0")
        else:
            self.a = a

s = Square(a=-2)
print(s, s.a)
