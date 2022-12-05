import random

from cat import Cat, Dog, Client
gosha = Cat(name="Gosha", age=5, sex="male")
print(gosha.get_age())
print(gosha.get_sex())
print(gosha.get_name())

max = Dog("max", "male", 3)
print(max.get_age())
print(max.get_name())
print(max.get_pet())

clients = []
for i in range(10):
    name = 'Клиент' + str(i)
    surname = 'Иванов' + str(i)
    city = 'Москва'
    balance = 100 * i + random.randint(10, 50)
    clients.append(Client(name, surname, city, balance))

for cl in clients:
    print(cl.get_info())

