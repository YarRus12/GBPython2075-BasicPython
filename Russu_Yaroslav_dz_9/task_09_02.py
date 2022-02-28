
class Road:
    #Атрибуты класса length (длина), width (ширина):
    def __init__(self, length: int, width: int):
        self._length = int(length)
        self._width = int(width)
        """конструктор класса
        :param length: длинна в метрах
        :param width: ширина в метрах
        """

    def calculate(self, height: int = 5, mass_m_2: int = 25) -> int:
        """
        считает массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param hight: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: int значение тонн, дробная часть если есть НЕ учитывается
        """
        height = float(height/100) #Переводим сантиметры в метры
        mass_m_2 = float(mass_m_2/1000) #переводим кг в тонны
        return int(self._length * self._width * height * mass_m_2)

if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')



