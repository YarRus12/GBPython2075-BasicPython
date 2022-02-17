import sys
import json
from itertools import zip_longest
def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    user_string = []
    hobbies_string = []
    with open(path_users_file, 'r', encoding='utf-8') as users:
        for line in users:
            #Данные их файла считаываются с '\n', поэтому разбиваем строку и забирает первый элемент
            #Убираем из строки запятые, что получить полное фио
            user_string.append(line.replace(',', '').split('\n')[0])
    with open(path_hobby_file, 'r', encoding='utf-8') as hobbies:
        for line in hobbies:
            #Данные их файла считаываются с '\n', поэтому разбиваем строку и забирает первый элемент
            #Остальные элементы разделяем на списки
            hobbies_string.append(((line.split('\n')[0]).split(', ')))
    #Если длина списка хобби получилась больше длинны пользователей, то вызываем функцию exit() из модуля sys
    if len(user_string) < len(hobbies_string):
        sys.exit(1)
    return dict(zip_longest(user_string, hobbies_string, fillvalue=None))

dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
print()