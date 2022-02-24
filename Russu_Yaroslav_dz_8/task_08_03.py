"""Написать декоратор для логирования типов позиционных аргументов функции, например:
"""
def type_logger(func):
    def class_type(*args):
        result = [type(i) for i in args]
        print(*zip(args, result), sep=', ')
    return class_type

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5, 6, 10)
