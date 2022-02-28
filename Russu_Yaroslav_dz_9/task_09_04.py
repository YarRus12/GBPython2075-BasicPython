
"""Задание 4
Реализуйте базовый класс Car:


добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля по формату в документации метода, если атрибут is_police равен True, то при вызове метода выводить в stdout дополнительно второе сообщение Вруби мигалку и забудь про скорость!;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) в stdout должно выводиться сообщение о превышении скорости Alarm!!! Speed!!!, если превышения нет, то стандартное сообщение из родительского класса.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
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
        self.speed += self.speed + 15
        return f'Машина {self.name} повысила скорость на 15: {self.speed}'

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        return f'{self.name} остановилась'

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction == 'направо' or  direction == 'налево' or direction == 'прямо' or direction == 'назад':
            return f'{self.name}: движется {direction}'
        else:
            raise ValueError(f'Нераспознанное направление движения')


    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


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
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    #sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """