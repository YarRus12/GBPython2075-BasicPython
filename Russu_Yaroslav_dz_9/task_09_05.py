
class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title
    def draw(self) -> None:
        print(f'Запуск отрисовки')

class Pen(Stationery):

    def draw(self) -> None:
        print(f'приступил к отрисовке объекта "Ручка"')

class Pencil(Stationery):

    def draw(self) -> None:
        print(f'приступил к отрисовке объекта "Карандаш"')

class Handle(Stationery):

    def draw(self) -> None:
        print(f'приступил к отрисовке объекта "Маркер"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
print()