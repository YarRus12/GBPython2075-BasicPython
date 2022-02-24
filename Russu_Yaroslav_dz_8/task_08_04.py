"""Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным целочисленным значением, включая 0.

Примечание: сможете ли вы замаскировать работу декоратора?

ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
def type_logger(func):
    def class_type(*args):
        result = [type(i) for i in args]
        print(*zip(args, result), sep=', ')
    return class_type

def val_checker(func):
    def checker(args):
        if len(args) == len([int(i) for i in args]):
            pass
        else:
            raise ValueError("Напишите имя проекта, и через запятую можете указать другую директорию")
        return checker
@val_checker(val_checker)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))