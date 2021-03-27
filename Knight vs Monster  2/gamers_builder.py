from backpack import Backpack
from gamer_types_factory import ArcherFactory, WizardFactory, WarriorFactory
import random
from validation import valid_input
from memento import Memento, ConcreteMemento


class Director:
    """Директор."""
    __builder = None

    def set_builder(self, builder):
        """Задание строителя."""
        self.__builder = builder

    def get_gamer(self):
        """Постройка игрока."""
        gamer = Gamer()
        gamer.health = self.__builder.get_health(self)
        gamer.power = self.__builder.get_power(self)
        gamer.backpack = self.__builder.get_backpack(self)
        gamer_type = self.__builder.get_gamer_type(self)
        gamer.set_gamer_type(gamer_type)


        return gamer


class Gamer:
    """Постройка игрока."""
    def __init__(self, killed_enemies=0, gamer_type=''):
        self._killed_enemies = killed_enemies
        self._backpack = Backpack()
        self.power = 0
        self._gamer_type = gamer_type
        self._health = random.randint(1, 10)

    def count_killed_enemies(self) -> int:
        self._killed_enemies += 1

    def set_gamer_type(self, gamer_type) -> str:
        self._gamer_type = gamer_type

    def setpower(self, power) -> int:
        self.power = power

    def set_backpack(self) -> int:
        self._backpack = Backpack().get_backpack()

    def set_health(self, health) -> int:
        self._health = health

    def print_specification(self) -> None:
        print(f"Раса - {self._gamer_type}")
        print(f"Жизней {self._health}")

    def update_health(self, enemy_toolpower: int) -> bool:
        self._health = self._health - int(enemy_toolpower)
        self.is_alive()

    def is_alive(self) -> bool:
        if self._health <= 0:
            return False
        else:
            return True

    def save(self) -> Memento:
        """
        Сохраняет текущее состояние внутри снимка.
        """
        return ConcreteMemento(self._health, self._killed_enemies, self._gamer_type, self._backpack.get_backpack().copy())

    def restore(self, memento: Memento) -> None:
        """
        Восстанавливает состояние Создателя из объекта снимка.
        """

        self._health = memento.get_health()
        self._killed_enemies = memento.get_killed_enemies()
        self._gamer_type = memento.get_gamer_type()
        self.power = memento.get_power()
        self._backpack = memento.get_backpack()
        print(f"Восстановлено состояние из тотема ")


class Builder:

    def get_health(self) -> None: pass

    def get_gamer_type(self) -> None: pass

    def get_backpack(self) -> dict: pass

    def get_killed_enemies(self) -> None: pass

    def get_power(self) -> None: pass

    def get_is_alive(self) -> None: pass


class HeroBuilder(Builder):

    def get_health(self, health=10) -> int:
        return health

    def get_killed_enemies(self) -> int:
        killed_enemies = 10
        return killed_enemies

    def get_gamer_type(self) -> str:
        self.gamer_type = GamerType.get_type(self, set_hero_type())
        return self.gamer_type

    def get_power(self):
        """Сила защиты."""
        self.power = random.randint(1, 20)
        return self.power

    def get_backpack(self):
        backpack = Backpack()
        return backpack


class MonsterBuilder(Builder):

    def get_health(self):
        self.health = random.randint(1, 20)
        return self.health

    def update_health(self, hitpower: int) -> int:
        self.health = self.health - hitpower
        return self.health

    def get_power(self):
        power = random.randint(1, 10)
        return power

    def get_gamer_type(self) -> str:
        self.gamer_type = GamerType.get_type(self, set_monster_type())
        return self.gamer_type


# Gamer parameters
class Health:
    pass


class Power:
    pass


class MagicTools:
    pass


class GamerType:
    def __init__(self):
        pass

    def get_type(self, z) -> str:
        a = z.create_GamerType()
        type = a.set_gamer_type()
        return type


type_to_factory_mapping = {
    "Лучник": ArcherFactory,
    "Волшебник": WizardFactory,
    "Воин": WarriorFactory
}

GamerType_type_list = {1: "Лучник", 2: "Волшебник", 3: "Воин"}


def user_choice() -> str:
    """Пользователь выбирает тип своего героя."""
    while True:
        b = input(f"Выбери своего героя: {GamerType_type_list}\n")
        if valid_input(b):
            if 0 < int(b) <= len(GamerType_type_list):
                user_choice = GamerType_type_list[int(b)]
                return user_choice
            else:
                print("Ошибка ввода")


def set_hero_type() -> str:
    type = type_to_factory_mapping[user_choice()]()
    return type


def set_monster_type() -> str:
    random_monster = random.choice(list(GamerType_type_list.values()))
    type = type_to_factory_mapping[random_monster]()
    return type
