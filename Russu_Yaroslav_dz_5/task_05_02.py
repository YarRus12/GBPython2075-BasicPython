
def odd_nums(number: int) -> int:
    """Генератор, принимающий в себя n значение и возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    # pass заглушка больше не нужна
    return (x for x in range(1, number+1, 2))  # Возвращает весь генератор

n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))


#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration