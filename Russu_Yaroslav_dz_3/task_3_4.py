"""Боюсь, что вложенные словари, для меня преждевременны
Дорешаю немного позже"""


def thesaurus_adv(*args) -> dict:
    dict_out = {}
    letters = [i[0] for i in args]
    names = [i for i in args]
    divided_names = [i.split(' ') for i in names]
    surname_letter = list(set([i[1][0] for i in divided_names]))
    for i in range(len(surname_letter)):
        dict_out.setdefault(surname_letter[i], {})
    return dict_out
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
"""Боюсь, что вложенные словари, для меня преждевременны
Дорешаю немного позже"""