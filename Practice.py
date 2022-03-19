class Person:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
class FullInfo(Person):
    def get_info(self):
        Person = (f"{self.name}, {self.city}, статус: {self.status}")
        return Person
client = FullInfo('Иван Петров', "г.Москва", '"наставник"')
print(client.get_info())



