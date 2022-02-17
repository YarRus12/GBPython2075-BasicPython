def main(argv):
    program, position, new_value = argv
    line_len = 10
    position_mark = (int(position)-1) * (line_len + len('\n'))
    file_name = 'bakery.csv'
    with open(file_name, 'r+', encoding='utf-8') as f:
        last_line = f.seek(0, 2)
        if last_line <= position_mark:
            raise TypeError(f'Запись №{position} отстствует')
        else:
            f.seek(position_mark)
            f.write(f'{new_value.ljust(line_len," ")}\n')

if __name__== '__main__':
    import sys
    if len(sys.argv) == 3:
        exit(main(sys.argv))
    else:
        raise TypeError('Ожидались <номер записи для редактирования> и <новое значение>')