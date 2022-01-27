def transform_string(number: int) -> str:
    if number == 1  or (number > 20 and number%10 == 1):
        result = f'{number} процент'
    elif (number > 1 and number < 5) or (number > 20 and number%10 > 1 and number%10 <5):
        result = f'{number} процента'
    else:
        result = f'{number} процентов'
    return result


for n in range(1, 101):
    print(transform_string(n))