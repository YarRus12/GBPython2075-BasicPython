import requests

def currency_rates(code: str):
    """ Функция показывает курс валюты на сайте ЦБРФ. Функция принимает в себя  код валюты,
    а возвращает значение валюты"""
    #Применим метод get() из библиотеки request для получения данных с URL и сохраним в переменную response
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    #Выполним проверку булева значения входит ли значение кода состояния в диапазон 200-399
    if response.ok:
        #Декодируем содержимое response в юникод, encoding устанавливается по дефолту
        response_text = response.text
        # Используем метод поиска индекса первого вхождения значения в строку find()
        begin_index_of_code = response_text.find(code)
        #Выполняем проверку есть ли запрашиваемый код валюты на странице
        if begin_index_of_code != -1:
            # Срезаем строку от места вхождения индекса до конца
            response_text = response_text[begin_index_of_code:]
            # Определяем место завершения записи о валюте
            end_index = response_text.find('</Value>')
            # Оставляем интересующий нас срез. Получаем строку с номиналом именем и значением
            response_text = response_text[:end_index]
            # Ищем номинал,значение: делаем срез строки от начала тега<> + длинна тега до закрытия тега</> и преобразуем в значение float
            nominal = int(response_text[response_text.find('<Nominal>') + len('<Nominal>'):response_text.find('</Nominal>')])
            # ',' не дает преобразовать str во float, поэтому меняем ее на '.'
            value = float(response_text[response_text.find('<Value>')+len('<Value>'):].replace(',', '.'))
            valute_info = round(value/nominal, 4)
            return valute_info
        #Если функции передали неправильное значение, то возвращаем значение None
        else:
            return None #Пропишу явно себе на будущее

print(currency_rates("USD"))
print(currency_rates("noname"))
print(currency_rates("AZN"))
print(currency_rates("KRW"))