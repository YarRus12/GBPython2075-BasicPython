class Clothes:
    def __init__(self):
        pass

    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, value: float = 0):
        self.value = value

    @property
    def calculate(self) -> float:
        return round(self.value/6.5+0.5, 2)

class Costume(Clothes):
    def __init__(self, high: float = 0):
        self.high = high

    @property
    def calculate(self) -> float:
        return round(self.high * 2 + 0.3, 2)

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3