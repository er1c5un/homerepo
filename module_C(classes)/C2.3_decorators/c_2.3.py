# создадим класс собаки
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
# т.к. метод помечен декоратором property, то нам не надо вызывать этот метод, чтобы получить результат
print(jane.human_age)