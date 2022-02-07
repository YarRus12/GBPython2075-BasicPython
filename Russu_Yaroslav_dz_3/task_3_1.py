
eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(value: str) -> str:
    """Функция принимает в себя строковое значение,
        обращается к внешнему словарю по ключу, именованному как value и возвращает перевод слова на русский язык,
        если ключ есть в словаре, есть ключа нет в словаре возвращает None"""
    str_out = eng_rus_dict.get(value, None)
    return str_out

print(num_translate("one"))
print(num_translate("eight"))

print('END')