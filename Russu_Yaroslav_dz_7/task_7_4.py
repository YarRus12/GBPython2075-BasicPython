
import os
def reserch(folder_name, direction = os.path.dirname(os.path.abspath(__file__))):
    """ Функция принимает значение папки и считает размер файлов"""
    dir = os.path.join(direction, folder_name)
    sizes = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            sizes.append(os.stat(os.path.join(root,file)).st_size)
    dict_keys = 100, 1000, 10000, 100000
    more_hund = 0
    more_th = 0
    more_ten_th = 0
    more_hund_th = 0
    for num in sizes:
        if num < 1000:
            more_hund +=1
        if num < 10000:
            more_th += 1
        if num < 100000:
            more_ten_th += 1
        if num > 100000:
            more_hund_th += 1
    dict_values = more_hund, more_th, more_ten_th, more_hund_th
    return dict(zip(dict_keys, dict_values))

print(reserch('trash_folder'))
