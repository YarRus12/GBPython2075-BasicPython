
class Store:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

class Orgtech:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

    class Printer(Orgtech):
        def __init__(self, name, price, quantity, cartrige):
            super().__init__(name, price, quantity)
            self.series = cartrige

    class Scaner(Orgtech):
        def __init__(self, name, price, quantity, resolution):
            super().__init__(name, price, quantity)
            self.resolution = resolution

    class Xerox(Orgtech):
        def __init__(self, name, price, quantity, color=False):
            super().__init__(name, price, quantity)
            self.color = color

print()