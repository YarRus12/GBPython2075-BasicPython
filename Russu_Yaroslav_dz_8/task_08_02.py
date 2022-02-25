"""Написать регулярное выражение для парсинга файла логов web-сервера из
ДЗ 6 урока nginx_logs.txt для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?"""

import os
import re

def log_pasing(folder):
    """ Функция-костыль принимает в себя путь до файла, разбивает строки на блоки информации
    и печатает результат"""
    with open(folder, 'r', encoding='utf-8') as logs:
        for i in logs:
            parsed_raw = []
            trush = []
            remote_addr = re.findall(r"^(\S+)", i)
            request_datetime = re.findall(r"\[([\w:/]+\s[+\-]\d{4})\]", i)
            request_type = re.findall(r'"(\S+)', i)[0]
            requested_resource = (re.findall(r'/(\S+)\s*(\S+)?\s*"', i)[1])[0]
            response_code = (re.findall(r'" (.+) "', i)[0])[0:3]
            response_size = ((re.findall(r'" (.+) "', i))[0])[1]
            parsed_raw = remote_addr, request_datetime, request_type, requested_resource, response_code, response_size
            print(parsed_raw)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder_name = 'nginx_logs.txt'
path = os.path.join(BASE_DIR, folder_name)
log_pasing(path)

print()