# игровое поле в виде двумерного списка.

import random
import copy
import pprint

pp = pprint.PrettyPrinter(indent=4)


def gamepath(x):
    row = copy.deepcopy(x)
    index = random.randint(0, 5)
    items = ['обрыв', 'монетка', 'меч']
    random_item = random.choice(items)
    row[index] = random_item
    return row


if __name__ == '__main__':
    field = list()  # список игрового поля
    sublist = [""] * 6  # пустые вложенные списки

    for i in range(7):  # кол-во строк
        field.append(gamepath(sublist))
    pp.pprint(field)
