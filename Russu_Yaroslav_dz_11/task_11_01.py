
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = [i for i in day_month_year.split('-')]
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day_month_year):
        day, month, year = Data.extract(day_month_year)
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f' {Data.extract(day_month_year)} Дата указана верно'
                else:
                    raise ValueError(f'Ошибка в указании года')
            else:
                raise ValueError(f'Ошибка в указании месяца')
        else:
            raise ValueError(f'Ошибка в указании дня')



print(Data.valid('09-03-2022'))
#print(Data.valid('09-13-2022'))
#print(Data.valid('59-03-2022'))
#print(Data.valid('09-12-2025'))




