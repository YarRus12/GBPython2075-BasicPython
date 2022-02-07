def thesaurus(*args) -> dict:
    """Функция принимает в себя неопределенное число агрументов,
        создает две переменные: буквы и имена, для формирования словаря из букв(key) и имен(value)
        если очередная первая буква имени не является ключом словаря, то буква включается в ключи словаря,
        а имя становитс его значением, иначе имя имя присоединяется к уже существующим ключам"""
    dict_out = {}  # результирующий словарь значений
    letters = [i[0] for i in args]
    names = [i for i in args]
    for i in range(len(names)):
        dict_out.setdefault(letters[i], [])
        if letters[i] in dict_out:
            dict_out[letters[i]].append(names[i])
        else:
            dict_out.setdefault(letters[i], names[i])
    return dict_out
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Николай", "Вадим", "Павел"))

print('END')