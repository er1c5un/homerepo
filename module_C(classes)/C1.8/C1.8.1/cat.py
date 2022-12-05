class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return self.name, self.age

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.surname} {self.name}. {self.city}. Баланс: {self.balance}'

    def get_info(self):
        return f'{self.surname} {self.name}. {self.city}'

