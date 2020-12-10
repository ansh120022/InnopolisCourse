#Задание 5

"""def RemoveInstall(InputCommands:str):
    commands_list = InputCommands()
    commands_list_new = list(filter(lambda x: x !='install', commands_list))
    print(commands_list_new)


def InputCommands()-> str:
    print("Input")
    commands_list = input()
    RemoveInstall(commands_list)"""




#Задание 2

import random
import copy

def gamepath(x):
    row = copy.deepcopy(x)
    index = random.randint(0, 5)
    A = ['Обрыв', 'Монетка', 'Бинт', 'Яма', 'Батарейка']
    B = random.choice(A)
    row[index] = B
    return row

field = list()
base_row = [""] * 6

for r in range(7):
    field.append(gamepath(base_row))
print(field)



#Задание 3

import itertools

for i in range(0,9):
    items = list(itertools.combinations_with_replacement('ABCD', i))
    items = list(filter(lambda x: x.count('A') <= 2 and x.count('B') <= 2 and x.count('C') <= 2 and x.count('D') <= 2, items))
    permutations = list()
    for a in items:
        items_new ="".join(a)
        permutations += list(itertools.permutations(items_new)) #- перестановки длиной r из iterable.
    for z in list(set(permutations)):
        print ("".join(z))



#Задание 4


#Задание 1
items = ['А', 'Г', 'Ц', 'Ц', 'Т', 'А']

def convert(x):
    if x == 'А':
        return 'Т'
    if x == 'Г':
        return 'Ц'
    if x == 'Ц':
        return 'Г'
    if x == 'Т':
        return 'А'
    raise Exception("ОШИБКА")

new_list = list(map(convert, items))
print(new_list)

