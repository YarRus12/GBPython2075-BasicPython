
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

def num_translate_adv(value: str) -> str:
    """Функция принимает в себя строковое значение,
            проверяет является ли первая буква заглавной, если является, то приводит value к нижнему регистру
            потом обращается к внешнему словарю по ключу, именованному как value и возвращает перевод слова на русский язык с заглавной буквой в начале,
            если ключ есть в словаре, есть ключа нет в словаре возвращает None"""
    if value[0] == value[0].upper():
        try:
            str_out = eng_rus_dict.get(value.lower(), None).capitalize()
        except AttributeError:  # str_out по дефолту None, поэтому обязательно обрабатываем AttributeError
            str_out = None
    else:
        str_out = eng_rus_dict.get(value.lower(), None)
    return str_out

print(num_translate_adv("One"))
print(num_translate_adv("tWo"))
print(num_translate_adv("Twenty"))
print(num_translate_adv("eight"))
print(num_translate_adv("eleven"))

print('END')