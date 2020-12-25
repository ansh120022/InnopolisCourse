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
    raise Exception("Некорректные входные данные")


new_list = list(map(convert, items))
print(new_list)
