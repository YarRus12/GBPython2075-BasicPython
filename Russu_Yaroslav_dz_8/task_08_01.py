"""Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения
 извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
 Если адрес не валиден, выбросить исключение ValueError."""

import re


def email_parse(email: str) -> dict:
    """Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    parsed = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email)
    if not parsed:
        raise ValueError(f"wrong email: {email}")
    else:
        return dict(zip(["username", "domain"], parsed[0]))


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrains.ru'))
