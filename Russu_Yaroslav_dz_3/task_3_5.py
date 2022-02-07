

from random import choice
from random import sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    list_out = []
    for i in range(count):
        joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
        list_out.append(joke)
    return list_out

print(get_jokes(2))
print(get_jokes(10))
print('Конец первой функции')

# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, flag='No') -> list:
    """Усложненная функция принимает в себя число интераций по генерации предложений из трех словарей
    и флаг запрета повтора с дефолтным значением 'No', и возвращает список предложений"""
    list_out = []
    if flag == 'No':
        for i in range(count):
            joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
            list_out.append(joke)
    else:
        try: # Обработаем ошибку на случай, если count больше длинны списка
            sample(nouns, counts=None, k=len(nouns))
            sample(adverbs, counts=None, k=len(adverbs))
            sample(adjectives, counts=None, k=len(adjectives))
            for i in range(count):
                joke = f"{nouns[i]} {adverbs[i]} {adjectives[i]}"
                list_out.append(joke)
        except IndexError:
            list_out.append("А все шутки кончились =)")
    return list_out

print(get_jokes_adv(2))
print(get_jokes_adv(10, 'Yes'))
print('END')


