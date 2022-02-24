"""Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения
 извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
 Если адрес не валиден, выбросить исключение ValueError."""

import re

def email_parse(email: str) -> dict:
    """Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    #Первая групировка всех символов до знака @
    #Вторая групировка от @ до точки
    #Проверка наличия после точки 2 или 3 букв домена
    match_line = re.findall(r"([a-zA-Z0-9_-]+)@([\w_\.-]*\.[a-zA-Z-]{2,3})$", email)
    # Если нет совпадений, то 0 - False
    if not match_line:
        raise ValueError(f"wrong email: {email}")
    else:
        return dict(zip(["username", "domain"], match_line[0]))


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrains.com'))
    print(email_parse('yarruss@mail.ru'))
    print(email_parse('someone@geekbrainsru'))

print()
