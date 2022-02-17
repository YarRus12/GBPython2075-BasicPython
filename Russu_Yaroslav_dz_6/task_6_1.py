from pprint import pprint
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

pprint(list_out)
#print(type(list_out))#проверяем, что функция выдает <class 'list'>
#print(type(list_out[0]))#проверяем, что result состоит из элементов <class 'tuple'>
print()