
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
        def __init__(self, cartrige = 'CA99'):
            self.cartrige = cartrige

    class Scaner(Orgtech):
        def __init__(self, resolution):
            self.resolution = resolution

    class Xerox(Orgtech):
        def __init__(self, color=False):
            self.color = color

print()