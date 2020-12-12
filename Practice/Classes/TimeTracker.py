import re
from datetime import timedelta

task_name1 = "Приготовление пиццы"
tags1 = ['cooking', 'pizza', 'tomatoes']
comment1 = 'Пятничная пицца'

task_name2 = "Решение задач"
tags2 = ['learning', 'python', 'homework']
comment2 = 'Ежедневная домашка'
tags_mask = '^[a-z]{1,20}$'


class Task:
    def __init__(self, name, duration, comment, tags):
        self.name = name
        self.duration = duration
        self.comment = comment
        if not self.validate_tags(tags):
            raise Exception ("Ошибка в теге")
        self.tags = tags

    def validate_tags(self, tags):
        for i in tags:
            if re.fullmatch(tags_mask, i):
                continue
            else:
                return None
        return tags

    def display_info(self):
        print(self.__str__())

    def __add__(self, other):
        """Задание 4."""
        if self.comment == other.comment:
            self.duration = self.duration + other.duration
            self.tags = list(set(self.tags + other.tags))
        return self

    def __str__(self):
        """Задание 5."""
        return "Задача: {} \t Продолжительность: {} \nКомментарий: {} \nТэги: {}".format(self.name, self.duration,
                                                                                         self.comment, self.tags)


class Calendar(Task):
    """Задание 6"""

    def __init__(self, date, name, duration, comment, tags):
        super().__init__(name, duration, comment, tags)
        self.date = date

    def __str__(self):
        return "Задача: {} \t Дата {}\t Продолжительность: {} \nКомментарий: {} \nТэги: {}".format(self.name,
                                                                                                   self.date,
                                                                                                   self.duration,
                                                                                                   self.comment,
                                                                                                   self.tags)
    def __add__(self, other):
        """Подсчёт потраченного времени за дату."""

        if self.date == other.date:
            return self.date, self.duration + other.duration


task1 = Task(task_name1, timedelta(minutes = 29), comment1, tags1)
# print(task1)
task2 = Task(task_name2, timedelta(minutes = 19), comment1, tags2)

print(task1 + task2)


# task3 = Calendar('01.09.2021', task_name2, 90, comment1, tags2)
# print(task3)

#task4 = Calendar('01.09.2021', task_name1, 50, comment2, tags1)

#print(task3+task4)
