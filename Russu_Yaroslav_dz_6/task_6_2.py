def get_parse_attrs(line: str) -> tuple:
    """Функция принимает в себя строку и разбивает ее строковыми методами на переменные.
    объединяет их в кортежи и возвращает кортеж"""
    # Вычленяем remote_addr срезом до первого пробела
    remote_addr = line.split(' ')[0]
    # Вычленяем request_type от первого вхождения двойных кавычек до символа слеш
    request_type = ((line.split('"')[1]).split("/")[0]).strip()
    # Вычленяем requested_resource от первого вхождения пробела после двойных кавычек пробела
    requested_resource = ((line.split('"')[1]).split(" ")[1]).split(" ")[0]
    # двойные объединяют строковые переменные в кортеж
    return (remote_addr, request_type, requested_resource)

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

def max_ip(uniq_ip: set, ip_all: list) -> tuple:
    """Функция определяет элемент списка с максимальным количеством вхождений
    На вход функция принимает сет уникальных значений и список всех ip адресов
    На выход возвращает кортеж из ip с максимальным количеством вхождений и число его вхождений"""
    max_ip = []
    max_number = 0
    for i in uniq_ip:
        number = ip_all.count(i)
        if number > max_number:
            max_ip, max_number = i, number
    return (max_ip, max_number)

uniq_ip = set([i[0] for i in list_out])
ip_all = list([i[0] for i in list_out])
ip, number = max_ip(uniq_ip, ip_all)
print(f'Самый главный спамер это пользователь с id: {ip}, его запросы встречаются {number} раз')
print()