"""*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

Например:

>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?"""


def thesaurus_adv(*args) -> dict:
    dict_out = {}
    letters = [i[0] for i in args]
    names = [i for i in args]
    divided_names = [i.split(' ') for i in names]
    surname_letter = list(set([i[1][0] for i in divided_names]))
    for i in range(len(surname_letter)):
        dict_out.setdefault(surname_letter[i], {})
    for x in range(len(divided_names)):
        dict_out[surname_letter].setdefault(divided_names[0][i], [)
    #    if surname_letter[i] in dict_out:
    #        dict_out[surname_letter[i]].append(' '.join(divided_names[i]))
    #    else:
    #        dict_out.setdefault(surname_letter[i], names[i])
    return dict_out
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))