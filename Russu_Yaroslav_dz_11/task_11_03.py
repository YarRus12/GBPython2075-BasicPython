
class Error:
    def __init__(self, *args):
        self.users_list = []

    def my_input(self):
        #Функция принимает в себя позиционные агрументы
        #Проверяет являются ли они числами. Введенные числа включат в итоговый список.
        #А при вводе не числе предупреждают, что введенные аргументы - недопустимы
        input_value = []
        while True:
            input_value = input('Введите значения и нажмите Enter, для завершения введите Stop: ')
            if input_value.lower() == 'stop':
                break
            try:
                self.users_list.append(int(input_value))
            except:
                print(f'Недопустимое значение')

        return f'Всего введено {len(self.users_list)} числовых значений(-я): {self.users_list}'

try_except = Error(1)
print(try_except.my_input())