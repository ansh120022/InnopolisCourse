"""Поставлена задача подготовить тестовые случаи для программы,
Программа находится в разработке и должна будет принимать слово составленное из букв A,B,C,D.
Каждая буква может повторяться не более 2ух раз.
Сгенерировать все возможные позитивные тестовые входные данные.
Дополнить негативными тестовыми данными.
Записать результат в файл или вывести на экран."""

import itertools

for i in range(0,9):
    items = list(itertools.combinations_with_replacement('ABCD', i)) # все комбинации
    items = list(filter(lambda x: x.count('A') <= 2 and x.count('B') <= 2 and x.count('C') <= 2 and x.count('D') <= 2, items))# из них лямбда-выражением отбираем только нужные
    permutations = list()
    for a in items:
        items_new ="".join(a)
        permutations += list(itertools.permutations(items_new)) #- перестановки длиной r из iterable.
    for z in list(set(permutations)):
        print ("".join(z))


