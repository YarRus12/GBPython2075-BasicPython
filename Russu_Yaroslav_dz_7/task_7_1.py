import os
def project_dir_sample(BASE_DIR, folder_name):
    """Функция принимает на вход основную директорию и имя корневой папки проекта,
    выполняет проверку наличия в корневой папки папок для конфигурации,
     и если они отсутствут добавляет их в корневую папку проекта"""
    if not os.path.exists(folder_name):
        main_folder = os.path.join(BASE_DIR, folder_name)
        os.makedirs(main_folder, exist_ok=True)
    else:
        print(f'Такой проект уже существует')
    if not os.path.exists('settings'):
        f_settings = os.path.join(main_folder, 'settings')
    if not os.path.exists('mainapp'):
        f_mainapp = os.path.join(main_folder, 'mainapp')
    if not os.path.exists('adminapp'):
        f_adminapp = os.path.join(main_folder, 'adminapp')
    if not os.path.exists('authapp'):
        f_authapp = os.path.join(main_folder, 'authapp')
    os.makedirs(f_settings, exist_ok=True)
    os.makedirs(f_mainapp, exist_ok=True)
    os.makedirs(f_adminapp, exist_ok=True)
    os.makedirs(f_authapp, exist_ok=True)
    print(f'Заготовка для проекта {folder_name} готова')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_dir_sample(BASE_DIR, 'my_project')

if __name__ == '__project_dir_sample__':
    import sys
    if len(sys.argv) == 1:
        exit(project_dir_sample(sys.argv))
    else:
        raise TypeError("Напишите имя проекта")
print()


