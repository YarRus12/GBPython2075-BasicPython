
class DivisionByZero:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    def divide_by_null(divider, dividend):
        try:
            return (divider / dividend)
        except :
            return (f"Ошибка! Деление на ноль недопустимо")


print(DivisionByZero.divide_by_null(100, 0))
print(DivisionByZero.divide_by_null(100, 1))
print(DivisionByZero.divide_by_null(100, 3))
print()