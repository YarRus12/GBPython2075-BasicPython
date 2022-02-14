tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Георгий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def check_gen(tutors: list, klasses: list):
    """ Функця принимает в себя два списка и возвращает пары кортежей tutor и klass,
     если число итераций менее длины klasses, иначе пару tutor и None.
     Количество итераций не больше длины списка tutors"""
    for i in range(len(tutors)):
        yield ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None))

generator = check_gen(tutors, klasses)
""" Выполняем проверку типа """
print(type(generator))# result: "<class 'generator'>"

for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

print('END')
print()
