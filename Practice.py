class Person:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
class FullInfo(Person):
    def get_info(self):
        person1 = (f"{self.name},{self.city},{self.status}")
        return person1
client=person1('Иван Петров', "г.Москва",'"наставник"')
print(client.get_info())


