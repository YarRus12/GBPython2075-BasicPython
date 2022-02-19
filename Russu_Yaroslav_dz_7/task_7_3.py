import os

def move_direction(name_old_dir, name_new_dir, direction = os.path.dirname(os.path.abspath(__file__))):
    """Функция принимает в себя папку источник и название новой папки
    и переносит файлы папки источника в новую папку
    !!! К сожалению она не отлажена, да она выполняет поставленную задачу,
    но без обработки FileExistsError выдает ошибку!!!"""
    import shutil
    old_dir = os.path.join(direction, name_old_dir)
    new_dir = os.path.join(direction, name_new_dir)
    files = os.listdir(old_dir)
    try:
        for folder in files:
            if folder != str(name_new_dir):
                if os.path.exists(new_dir):
                    os.makedirs(new_dir, exist_ok=True)
                    shutil.copytree(old_dir, new_dir, symlinks=False)
                    print(f'Папка {folder} скопирована в {new_dir}')
                else:
                    shutil.copytree(old_dir, new_dir, symlinks=False)
                    print(f'Папка {folder} скопирована в {new_dir}')
    except FileExistsError:
        print(f'А как бороться с этой бедой я узнаю в следующей серии')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
move_direction('my_project', 'my_project/templates')

if __name__ == '__move_direction__':
    import sys
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        exit(move_direction(sys.argv))
    else:
        raise TypeError("Укажите папку-источник, название целевой папки через запятую")
print()
