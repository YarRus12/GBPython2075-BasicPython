""" ЗАГОТОВКА"""
"""
decimal позволяет записывать десятичные дроби с максимальной точностью,
что крайне важно для работы с деньгами"""
import sys
import requests
import requests.utils
import typing
from pyquery import pyquery as pq
import xml.etree.ElementTree as etree
from pprint import pprint

def send_request(url) ->requests.Response:
    response = requests.get(url)
    if not response.ok:
        print('Чьорт побьери, все пропало, шеф!')
        sys.exit(0)
    return response

def extract_data(tag: str, url) -> typing.list:
    res = send_request(url)
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return curs_val.xpath(f'//Valute/{tag}/text()')

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
if __name__ == '__main__':
    name_valutes = extract_data('USD', url)
    pprint(name_valutes)


#def currency_rates(code: str) -> float:
#    """"Функция должна принимать в себя код валюты и возвращает курс валютной пары <валюта>/рубль """
#    # ваша реализация здесь
#    result_value = 1.11  ## здесь должно оказаться результирующее значение float/decimal
#    return result_value

#print(currency_rates("USD"))
#print(currency_rates("noname"))


