def convert_name_extract(list_in: list) -> list:
    list_out = []
    for i in my_list:
        list_out.append('Привет, '+i.split(' ')[-1].capitalize() + '!')
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)