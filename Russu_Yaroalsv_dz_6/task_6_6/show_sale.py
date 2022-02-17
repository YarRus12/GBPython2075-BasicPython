
def main(start: int, finish: int):
    file_name = '../task_6_7/bakery.csv'
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readline()
        line_count = 1
        while (line_count <= finish) or (finish == 0 and line):
            if line_count >= start:
                print(line.strip())
            line = f.readline()
            line_count += 1

if __name__ == '__main__':
    import sys
    #Если запрос содержит только наименование файла, то в функция исполняется
    #с первой по последнюю строку
    if len(sys.argv) == 1:
        exit(main(1, 0))
    #Если запрос содержит только наименование файла и начальную строку,
    #то в функция исполняется с указанной строки по последнюю строку
    elif len(sys.argv) == 2:
        prog, start = sys.argv
        exit(main(int(start), 0))
    # Если запрос содержит наименование файла, начальную и коненые строки,
    # то в функция выводит только диапазон указанных строк
    elif len(sys.argv) == 3:
        prog, start, finish = sys.argv
        exit(main(int(start), int(finish)))
    else:
        raise TypeError("Ожидались параметры ввода")