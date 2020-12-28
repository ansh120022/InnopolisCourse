from abc import ABC, abstractmethod
import random


class GamerType(ABC):
    """Абстрактный класс типа игрока."""

    @abstractmethod
    def use_protection(self) -> None:
        pass

    def update_health(self) -> None:
        pass


class Archer(GamerType):
    """Конкретный тип игрока - Лучник"""

    def set_gamer_type(self) -> str:
        self.gamer_type = 'Лучник'
        return self.gamer_type

    def use_protection(self) -> str:
        protection_power = random.randint(1, 20)
        return f"Сработала защита лучника с силой {protection_power}"


class Wizard(GamerType):
    """Конкретный тип игрока - Волшебник"""

    def set_gamer_type(self) -> str:
        self.gamer_type = 'Волшебник'
        return self.gamer_type

    def use_protection(self) -> str:
        protection_power = random.randint(1, 20)
        return f"Сработала защита заклинания с силой {protection_power}"


class Warrior(GamerType):
    """Конкретный тип игрока - Воин"""

    def set_gamer_type(self)  -> str:
        self.gamer_type = 'Воин'
        return self.gamer_type

    def use_protection(self)  -> str:
        protection_power = random.randint(1, 20)
        return f"Сработала защита воина с силой {protection_power}"


class GamerTypeFactory(ABC):
    """Абстрактная фабрика игрока."""

    @abstractmethod
    def create_GamerType(self) -> None:
        """Создание абстрактного игрока."""
        pass


class ArcherFactory(GamerTypeFactory):
    """Конкретная фабрика лучников."""

    def create_GamerType(self) -> object:
        return Archer()


class WizardFactory(GamerTypeFactory):
    """Конкретная фабрика волшебников."""

    def create_GamerType(self)-> object:
        return Wizard()


class WarriorFactory(GamerTypeFactory):
    """Конкретная фабрика воинов."""

    def create_GamerType(self)-> object:
        return Warrior()
