class Square:
    _x = None

    def __str__(self):
        return f'square with side {self.x}'

    @property
    def area(self):
        return self.x * self.x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value > 0:
            self._x = value
        else:
            raise ValueError("Side of the square must be > 0")


class SquareFactory:

    @staticmethod
    def make_square():
        return Square()


sq1 = SquareFactory.make_square()
sq1.x = 7
print(sq1)
print(sq1.area)

