def fibonacci(n) -> tuple:
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

for i in fibonacci(10):
    print(i)


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

val = countdown(5)
next(val)



my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)

"""Генераторы можно применять для вычитывания файлов из директории"""