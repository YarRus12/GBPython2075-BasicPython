
def convert_list_in_str(list_in: list) -> str:
    n_list = []
    extra = 0
    for i in list_in:
        str_out = []
        if i.isdigit() == True and len(str(i)) < 2:
            i = f'"{"0"+i}"'
            str_out += ''.join(i)
        elif i.isdigit() == True:
            i = f'"{i}"'
            str_out += ''.join(i)
        else:
            if i.isalpha():
                str_out += ''.join(i)
            else:
                out = []
                for j in i:
                    if j.isdigit() == True:
                        j = f'{"0"+j}'
                        out.append(j)
                    else:
                        out.append(j)
                line = f'"{"".join(out)}"'
                str_out += ''.join(line)
        n_list.append(''.join(str_out))
    return n_list

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(*result)
