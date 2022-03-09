"""Задание 5
Продолжить работу над заданием 4.

Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь)."""


class Sklad:
    def __init__(self):
        self.list = []

    def add_to(self, Orgtech):
        self.list.append(Orgtech)

class Orgtech:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f'{self.name}-{self.price}-{self.quantity}'


class Printer(Orgtech):
    def __init__(self, name, price, quantity, cartrige):
        super().__init__(name, price, quantity)
        self.series = cartrige
    def __str__(self):
        return f'{self.name}-{self.price}-{self.quantity}-{cartrige}'

class Scaner(Orgtech):
    def __init__(self, name, price, quantity, resolution):
        super().__init__(name, price, quantity)
        self.resolution = resolution
    def __str__(self):
        return f'{self.name}-{self.price}-{self.quantity}-{self.resolution}'

class Xerox(Orgtech):
    def __init__(self, name, price, quantity, color=False):
        super().__init__(name, price, quantity)
        self.color = color
    def __str__(self):
        return f'{self.name}-{self.price}-{self.quantity}-{self.color}'


sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90, 1080)
sklad.add_to(scaner)
printer = Printer('ms', '400', 97, 'C5-11')
sklad.add_to(scaner)
xerox = Xerox('ks', '1000', 82)
sklad.add_to(xerox)
# выводим склад
for i in sklad.list:
    print(i, end='\n')

print()