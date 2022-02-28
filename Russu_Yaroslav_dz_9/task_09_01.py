
class TrafficLight:
    """ Функция выполняет переключение цвета светофора"""
    #Глобальный атрибут класса. В тексте ДЗ нет указание, что это строка,
    #поэтому сделаем словарь со значениями условий задачи
    __color = {'red': 4,
             'yellow': 2,
             'green': 3}
    def running(self):
        import time
        #Присвоим локальной переменной метода значение глобальной переменной
        color = TrafficLight.__color
        for key in color:
            time_left = color[key]
            while time_left > 0:
                print(f'{key} {time_left}')
                #Отложение исполнения программы
                time.sleep(1)
                time_left -= 1
            print(f'Внимание! Зажигается другой цвет светофора!')


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()

print()


