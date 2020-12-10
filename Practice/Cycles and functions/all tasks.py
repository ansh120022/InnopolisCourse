# задача4

def my_function(**my_kwargs):
    if "name" in my_kwargs.keys() and "city" in my_kwargs.keys() and "job" in my_kwargs.keys():
        print(my_kwargs["name"] +' '+my_kwargs["city"] + ' '+ my_kwargs["job"])

my_function(name="Саша", city="Innopolis", job="job")

#задача 3
def checking_text(text: str, *my_args: Any) -> bool:
    for i in my_args:
        if i not in text:
            return False
    return True

# задача2
def fibonacci(n) -> tuple:
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

print(fibonacci(20))


#задача 1
for i in range(1,21,1):
    if i%2 == 0 or (i%10 + i//10)%2 == 0:
        print(i**2)
    else:
        print(i**3)


#Задача 6

import sqlite3

conn = sqlite3.connect('task.db')

def CreateTable():
    """Функция которая создаёт таблицу"""
    c = conn.cursor()
    # ВАШ КОД ЗДЕСЬ
    c.execute("""
    DROP TABLE IF exists Expenses;""")
    c.execute("""CREATE TABLE IF NOT EXISTS Expenses (id integer PRIMARY KEY AUTOINCREMENT, date numeric, name text, money real);""")


CreateTable()

def InsertData():
    c = conn.cursor()
    print("Введите имя")
    name = input()
    print("Введите сумму")
    money = input()
    print("Введите дату")
    date = input()
    c.execute(f"""
    insert into Expenses (name, money, date)
    values
    ('{name}', {money}, '{date}')
    ;""")

    conn.commit()

InsertData()
conn.close()