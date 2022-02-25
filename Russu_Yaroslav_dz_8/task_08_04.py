from functools import wraps

def adv_check(*argv):
    if len(argv) != 1:
        raise ValueError(f"Провалена проверка № 1 {argv}")
    #Проверка первого элемента именованного аргумента из кортежа
    if not isinstance(argv[0], int) or argv[0] <= 0:
        raise ValueError(f"Провалена проверка № 2 {argv[0]}")

def val_checker(func):
    """Функция принимает в себя функцию проверку значений позиционных аргументов
    и возвращает значения, соответствующие условию проверки"""
    def checker(main_func):
        @wraps(main_func)
        def wrapper(*args):
            # Передача аргументов в функцию adv_check
            func(*args)
            result = main_func(*args)
            return result
        return wrapper
    return checker


@val_checker(adv_check)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))

