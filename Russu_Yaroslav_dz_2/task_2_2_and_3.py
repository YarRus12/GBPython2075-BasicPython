def convert_list_in_str(list_in: list) -> str:
    n_list = []
    for i in list_in:
        str_out = []
        if i.isdigit() == True and len(str(i)) < 2:
            str_out.append('"')
            str_out.append('0' + i)
            str_out.append('"')
        elif i.isdigit() == True:
            str_out.append('"')
            str_out.append(i)
            str_out.append('"')
        else:
            if i.isalpha():
                str_out.append(i)
            else:
                out = []
                for j in i:
                    if j.isdigit() == True:
                        out.append('0' + j)
                    else:
                        out.append(j)
                str_out.append(''.join("'"))
                str_out.append(''.join(out))
                str_out.append(''.join("'"))
        n_list.append(''.join(str_out))
    return n_list

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(*result)
