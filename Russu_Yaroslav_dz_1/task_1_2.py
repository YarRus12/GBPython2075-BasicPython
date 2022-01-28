def sum_list_1(dataset: list) -> int:
    total_sum = 0 # большой локальный счетчик
    for i in dataset:
        number = i
        sum_i = 0 # малый локальный счетчик
        while i > 0:   #до тех пор пока очередное число больше нуля заполняем малый счетчик
            sum_i += i % 10 #добавляем к малому счетчику последнюю цифру
            i = i // 10 # отрезаем у числа последнюю цифру
        if sum_i % 7 == 0: #если малый счетчик делится на 7 без остатка, то добавляем его к большому локальному счетчику
            total_sum += number
    return total_sum

def sum_list_2(dataset: list) -> int:
    total_sum = 0
    for i in dataset:
        number = i
        i = i + 17 # новое условие - каждое число в numbers на входе в цикл увеличивается на 17
        sum_i = 0
        while i > 0:
            sum_i += i % 10
            i = i // 10
        if sum_i % 7 == 0:
            total_sum += (number+17) #поскольку прибавить нужно новое число, то в цикле прибавляем к старому 17 и добавляем к большому счетчику
    return total_sum



my_list = [i ** 3 for i in range(1,1000,2)] #генератор чисел в диапазоне от 1 до 999 с шагом 2
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)