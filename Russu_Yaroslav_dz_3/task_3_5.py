"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
ВНИМАНИЕ! Используйте стартовый код для своей реализации:

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
"""


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = ["здесь собранные шутки"]
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
# def get_jokes_adv(...) -> list:
#     # пишите реализацию здесь
#     return []