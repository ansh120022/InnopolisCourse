from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class Kafka(Subject):
    """
    Система, куда все команды пишут результаты своей работы
    """

    _state: int = 0
    """
    Соcтояние будет изменятся на положительное число поступающих сообщений
    """

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Kafka: добавлен консьюмер.\n")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Kafka: удалён консьюмер.\n")
        self._observers.remove(observer)

    """
    Методы управления подпиской.
    """

    def notify(self) -> None:
        """
        Запуск обновления в каждом подписчике.
        """

        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        self._state = randint(0, 10)

        print(f"Kafka: Поступили новые сообщения: {self._state}")
        self.notify()


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Получить обновление от субъекта.
        """
        pass


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class Website(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 0:
            print("Website: Прочитал новые сообщения\n")





if __name__ == "__main__":

    subject = Kafka()

    observer_a = Website()
    subject.attach(observer_a)


    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)