import os
import sys

def settings(main_folder):
    if not os.path.exists('settings'):
        f_settings = os.path.join(main_folder, 'settings')
        os.makedirs(f_settings, exist_ok=True)
        if not os.path.exists(os.path.join(f_settings, "__init.py__")):
            init_file = open(os.path.join(f_settings, "__init.py__"), "w")
            init_file.write("Init файл")
        if not os.path.exists(os.path.join(f_settings, "dev.py")):
            dev_file = open(os.path.join(f_settings, "dev.py"), "w")
            dev_file.write("Dev файл")
        if not os.path.exists(os.path.join(f_settings, "prod.py")):
            prod_file = open(os.path.join(f_settings, "prod.py"), "w")
            prod_file.write("Prod файл")

def mainapp(main_folder):
    if not os.path.exists('mainapp'):
        f_mainapp = os.path.join(main_folder, 'mainapp')
        os.makedirs(f_mainapp, exist_ok=True)
        if not os.path.exists(os.path.join(f_mainapp, "__init.py__")):
            init_file = open(os.path.join(f_mainapp, "__init.py__"), "w")
            init_file.write("Init файл")
        if not os.path.exists(os.path.join(f_mainapp, "models.py")):
            models_file = open(os.path.join(f_mainapp, "models.py"), "w")
            models_file.write("Models файл")
        if not os.path.exists(os.path.join(f_mainapp, "views.py")):
            models_file = open(os.path.join(f_mainapp, "views.py"), "w")
            models_file.write("Views файл")
        if not os.path.exists('templates'):
            f_templates = os.path.join(f_mainapp, 'templates')
            os.makedirs(f_templates, exist_ok=True)
            if not os.path.exists('mainapp'):
                f_mainapp = os.path.join(f_templates, 'mainapp')
                os.makedirs(f_mainapp, exist_ok=True)
                if not os.path.exists(os.path.join(f_mainapp, "base.html")):
                    base_file = open(os.path.join(f_mainapp, "base.html"), "w")
                    base_file.write("base.html файл")
                if not os.path.exists(os.path.join(f_mainapp, "index.html")):
                    base_file = open(os.path.join(f_mainapp, "index.html"), "w")
                    base_file.write("index.html файл")

def authapp(main_folder):
    if not os.path.exists('authapp'):
        f_authapp = os.path.join(main_folder, 'authapp')
        os.makedirs(f_authapp, exist_ok=True)
        if not os.path.exists(os.path.join(f_authapp, "__init.py__")):
            init_file = open(os.path.join(f_authapp, "__init.py__"), "w")
            init_file.write("Init файл")
        if not os.path.exists(os.path.join(f_authapp, "models.py")):
            models_file = open(os.path.join(f_authapp, "models.py"), "w")
            models_file.write("Models файл")
        if not os.path.exists(os.path.join(f_authapp, "views.py")):
            models_file = open(os.path.join(f_authapp, "views.py"), "w")
            models_file.write("Views файл")
        if not os.path.exists('templates'):
            f_templates = os.path.join(f_authapp, 'templates')
            os.makedirs(f_templates, exist_ok=True)
            if not os.path.exists('authapp'):
                f_authapp = os.path.join(f_templates, 'authapp')
                os.makedirs(f_authapp, exist_ok=True)
                if not os.path.exists(os.path.join(f_authapp, "base.html")):
                    base_file = open(os.path.join(f_authapp, "base.html"), "w")
                    base_file.write("base.html файл")
                if not os.path.exists(os.path.join(f_authapp, "index.html")):
                    base_file = open(os.path.join(f_authapp, "index.html"), "w")
                    base_file.write("index.html файл")




def project_dir_sample(folder_name: 'str', direction = os.path.dirname(os.path.abspath(__file__))):
    """Функция принимает на вход основную директорию и имя корневой папки проекта,
    выполняет проверку наличия в корневой папки папок для конфигурации,
     и если они отсутствут добавляет их в корневую папку проекта"""
    main_folder = os.path.join(direction, folder_name)
    if os.path.exists(folder_name):
        answer = input(f'Папка c именем "{folder_name}" уже существует.'
                       f'Дополнить ее папками со стандартными настройками проекта?'
                       f'Ваш ответ (YES/NO): ').lower()
        if answer == 'yes':
            settings(main_folder)
            mainapp(main_folder)
            authapp(main_folder)
            sys.exit(f'Папка "{folder_name}" дополнена стандарным настройками проекта')
        elif answer == 'no':
            sys.exit(f'Создайте проект с имененм отличным от "{folder_name}"')
        else:
            sys.exit(f'Что-то пошло не так! Кажется, вы не ответили на наш вопрос. '
                     f'Попробуйте назвать проект имененем отличным от "{folder_name}"')
    else:
        os.makedirs(main_folder, exist_ok=True)
        settings(main_folder)
        mainapp(main_folder)
        authapp(main_folder)
    print(f'Заготовка для проекта {folder_name} готова')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_dir_sample('my_project')

if __name__ == '__project_dir_sample__':
    import sys
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        exit(project_dir_sample(sys.argv))
    else:
        raise TypeError("Напишите имя проекта, и через запятую можете указать другую директорию")
print()


