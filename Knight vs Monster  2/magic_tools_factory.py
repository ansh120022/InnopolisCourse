"""Создание магических предметов."""

from __future__ import annotations
from abc import ABC, abstractmethod
import random


class Creator(ABC):

    @abstractmethod
    def factory_method(self) -> None:
        """Абстрактный фабричный метод"""
        pass

    def some_set_tool_attrs(self) -> str:
        tool = self.factory_method()
        result = tool.set_tool_attrs()

        return result


class ConcreteAppleCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Яблоко."""
        return Apple()


class ConcreteArrowsCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Стрелы."""
        return Arrows()


class ConcreteSwordCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Яблоко."""
        return Sword()


class ConcreteBookCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Книга заклинаний."""
        return Book()


class ConcreteTotemCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Тотем."""
        return Totem()


class ConcreteBowCreator(Creator):
    def factory_method(self) -> MagicTool:
        """Конкретный предмет Лук."""
        return Bow()


class MagicTool(ABC):

    @abstractmethod
    def set_tool_attrs(self) -> str:
        """Абстрактный метод, который будет у всех конкретных предметов."""
        pass


class Apple(MagicTool):
    def set_tool_attrs(self) -> str:
        """Яблочко."""
        tool = {}
        name = 'Яблочко'
        power = random.randint(1, 10)
        tool[name] = power
        return tool


class Arrows(MagicTool):
    def set_tool_attrs(self) -> str:
        """Стрелы."""
        tool = {}
        name = 'Стрелы'
        power = random.randint(1, 10)
        tool[name] = power
        return tool


class Sword(MagicTool):
    def set_tool_attrs(self) -> dict:
        tool = {}
        name = 'Меч'
        power = random.randint(1, 10)
        tool[name] = power
        return tool


class Book(MagicTool):
    def set_tool_attrs(self) -> dict:
        tool = {}
        name = 'Книга'
        power = random.randint(1, 10)
        tool[name] = power
        return tool


class Totem(MagicTool):
    def set_tool_attrs(self) -> str:
        name = 'Тотем'
        return name


class Bow(MagicTool):
    def set_tool_attrs(self) -> dict:
        tool = {}
        name = 'Лук'
        power = random.randint(1, 10)
        tool[name] = power
        return tool


def generate_magic_tool() -> str:
    """Запуск создания предметов."""
    type_to_factory_mapping = {
        "Яблочко": ConcreteAppleCreator,
        "Стрелы": ConcreteArrowsCreator,
        "Меч": ConcreteSwordCreator,
        "Книга": ConcreteBookCreator,
        "Тотем": ConcreteTotemCreator,
        "Лук": ConcreteBowCreator
    }
    magic_tools_list = ('Тотем', 'Лук', 'Яблочко', 'Стрелы', 'Книга', 'Меч')
    random_choice = random.choice(magic_tools_list)
    created_tool = type_to_factory_mapping[random_choice]().some_set_tool_attrs()
    return created_tool
