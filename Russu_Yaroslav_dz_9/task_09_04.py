
class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = self.is_police
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed += 15
        print(f'Машина {self.name} повысила скорость на 15: {self.speed}')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        print(f'{self.name} остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction == 'направо' or  direction == 'налево' or direction == 'прямо' or direction == 'назад':
            print(f'{self.name}: движется {direction}')
        else:
            raise ValueError(f'Нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police == True:
            print(f'{self.name}: текущая скорость {self.speed}')
            print(f'Вруби мигалку и забудь про скорость!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            print(f'Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')
class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            print(f'Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')
class SportCar(Car):
    pass
class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    #текущая скорость 120 км/час
    #Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """