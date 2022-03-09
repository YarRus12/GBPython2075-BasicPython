"""Задание 6
Продолжить работу над заданием 5.

Реализовать механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных!
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""

class Store:
    def __init__(self):
        self._dict = {}

    def add_to(self, Orgmachines):
        """добавляем в словарь обьект по его названию, в значении
        будет список оргтехники"""
        self._dict.setdefault(Orgmachines.group_name(), []).append(Orgmachines)


class Orgmachines:
    def __init__(self, *args):
        self.group = self.__class__.__name__
        try:
            self.name = input('Введите модель: ')
            self.price = int(input('Введите цену: '))
            self.quantity = int(input('Введите количество: '))
        except:
            raise ValueError(f'Недопустимое значение')
    def __str__(self):
        return f'{self.name} {self.price} {self.quantity}'
    def group_name(self):
        return f'{self.group}'

class Scaner(Orgmachines):
    def __init__(self):
        super().__init__()
        try:
            self.resolustion = int(input('Введите разрешение сканера (например 1080): '))
        except:
            raise ValueError(f'Недопустимое значение')
    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}, {self.resolustion}'

class Printer(Orgmachines):
    def __init__(self):
        super().__init__()
        try:
            self.cartridge = input('Введите модель картриджа: ')
        except:
            raise ValueError(f'Недопустимое значение')
    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}, {self.cartridge}'

class Xerox(Orgmachines):
    def __init__(self):
        super().__init__()
        try:
            self.color = input('Выполняет ли Xerox цветную печать? y/n: ')
        except:
            raise ValueError(f'Недопустимое значение')
    def __str__(self):
        return f'{self.name} {self.price} {self.quantity} {self.color}'


store = Store()
# создаем объект и добавляем
scaner = Scaner()
store.add_to(scaner)
xerox = Xerox()
store.add_to(xerox)
printer = Printer()
store.add_to(printer)
# выводим склад
for key, value in store._dict.items():
    print(key, ':', *value)
print()