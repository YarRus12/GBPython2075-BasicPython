import os

def move_direction(name_old_dir, name_new_dir, direction = os.path.dirname(os.path.abspath(__file__))):
    """Функция принимает в себя папку источник и название новой папки
    ищет среди полных путей всех файлов файлы в разрешением html и папки с найденными
     файлами в новую папку """
    import shutil
    old_dir = os.path.join(direction, name_old_dir)
    new_dir = os.path.join(direction, name_new_dir)
    for root, dirs, files in os.walk(old_dir):
        for file in files:
            if (file.endswith(".html")):
                dir = ((os.path.join(root,file)))
                html_dir = dir[:(dir.find('templates'))+len('templates')]
                shutil.copytree(html_dir, new_dir, symlinks=False, dirs_exist_ok=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
move_direction('my_project', 'my_project/templates')

if __name__ == '__move_direction__':
    import sys
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        exit(move_direction(sys.argv))
    else:
        raise TypeError("Укажите папку-источник, название целевой папки через запятую")
print()
