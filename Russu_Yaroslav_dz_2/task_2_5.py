from random import uniform
import copy

def transfer_list_in_str(list_in: list) -> str:
    str_out = []
    for i in list_in:
        i = str(float(i))
        rubles, penny = i.split('.')
        if len(penny) < 2:
            penny = '0' + penny
        str_out.append(''.join(f'{rubles} руб {penny} коп'))
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in

# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)

def sort_price_adv(list_in: list) -> list:
    list_out = copy.deepcopy(list_in)
    list_out.sort(reverse=True)
    return list_out

result_3 = sort_price_adv(my_list)
print(result_3)

def check_five_max_elements(list_in: list) -> list:
    list_out = copy.deepcopy(list_in)
    list_out.sort(reverse=True)
    return list_out[:5]
    # Если case был в применениии ранее написанных функций то:
    # return sort_price_adv(list_in)[:5]

result_4 = check_five_max_elements(my_list)
print(result_4)
