class Rectangle:
    def __init__(self, x: int = 0, y: int = 0, width: int = 50, height: int = 50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle x={self.x}, y={self.y}, width={self.width}, height={self.height}'

    def calc_area(self):
        return self.width * self.height

my_rect = Rectangle(10, 10, 100, 300)
print(my_rect)

print(f'Area of my_rect is {my_rect.calc_area()}')
