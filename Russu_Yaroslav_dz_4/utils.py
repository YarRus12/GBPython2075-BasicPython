import requests
import datetime

def time(response):
    """Отдельная функция для вычисления времени
    Принимает в себя результаты запроса на сайте.
    Возвращает время на странице"""
    if response.ok:
        response_text = response.text
        date_index = response.text.find('Date')
        day, month, year = (response_text[date_index + len('Date="'):response.text.find('name') - 2]).split('.')
        date = str(datetime.date(int(year), int(month), int(day)))
    return date


def currency_rates_adv(code: str):
    """ Функция показывает курс валюты на сайте ЦБРФ. Функция принимает в себя  код валюты,
    а возвращает значение валюты"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.ok:
        response_text = response.text
        begin_index_of_code = response_text.find(code)
        if begin_index_of_code != -1:
            response_text = response_text[begin_index_of_code:]
            end_index = response_text.find('</Value>')
            response_text = response_text[:end_index]
            nominal = int(response_text[response_text.find('<Nominal>') + len('<Nominal>'):response_text.find('</Nominal>')])
            value = float(response_text[response_text.find('<Value>') + len('<Value>'):].replace(',', '.'))
            valute_info = round(value / nominal, 4)
            return valute_info, time(response)
        else:
            return None

if __name__ == '__main__':
    currency_rates_adv()
    time()