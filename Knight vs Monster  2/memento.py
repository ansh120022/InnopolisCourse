from __future__ import annotations
from abc import ABC, abstractmethod
from backpack import Backpack

class Memento(ABC):
    """
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """

    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def get_killed_enemies(self) -> int:
        pass

    @abstractmethod
    def get_gamer_type(self) -> str:
        pass

    @abstractmethod
    def get_backpack(self) -> dict:
        pass


class ConcreteMemento(Memento):
    def __init__(self, health: int, killed_enemies: int, gamer_type: str, backpack: dict) -> None:
        self._health = health
        self._killed_enemies = killed_enemies
        self._gamer_type = gamer_type
        self._backpack = backpack


    def get_health(self) -> str:
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """
        return self._health

    def get_killed_enemies(self) -> str:
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """
        return self._killed_enemies

    def get_gamer_type(self) -> str:
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """

        return self._gamer_type

    def get_backpack(self) -> str:
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """

        return self._backpack


class Caretaker():
    """
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nВ тотеме сохранено текущее состояние")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print("Восстановлено сохpанённое состояние")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()