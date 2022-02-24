def result_type(expressions):
    for expression in expressions:
        print(f'{expression} - ', type(expression))
        print(isinstance(expression, int))
        print(dir(expression))


expressions = 15 * 3, 15 / 3, 15 // 2, 15 ** 2
result_type(expressions)
print()