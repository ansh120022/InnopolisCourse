import random
import string
import pprint

pp = pprint.PrettyPrinter(indent=2)


# Задача 1

def create_dictionary():
    keys = [create_string(5) for _ in range(9)]
    values = [create_string(5) for _ in range(9)]
    dictionary = dict(zip(keys, values))
    print(dictionary)
    return dict(dictionary)


def create_string(length):
    str_d = ''
    for i in range(length):
        i = random.choice(string.ascii_lowercase)
        str_d += i
    return str_d


create_dictionary()

# Задача 2 -- сделать в цикле

d1 = create_dictionary()
d2 = create_dictionary()
d3 = create_dictionary()

print(d1)
print(d2)

i = random.choice(list(d2.keys()))
d2[i] = d3

i = random.choice(list(d1.keys()))
d1[i] = d2

print("--------------------------")
print(i)
pp.pprint(d1)
