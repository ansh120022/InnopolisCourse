from backpack import Backpack
from gamer_types_factory import ArcherFactory, WizardFactory, WarriorFactory
import random
from validation import valid_input


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
        gamer_type = self.__builder.get_gamer_type(self)
        gamer.set_gamer_type(gamer_type)

        return gamer


class Gamer:
    """Постройка игрока."""
    def __init__(self, killed_enemies=0):
        self.backpack = Backpack()
        self.killed_enemies = killed_enemies
        self.power = 0
        self.health = random.randint(1, 10)

    def count_killed_enemies(self) -> int:
        self.killed_enemies += 1

    def set_gamer_type(self, gamer_type) -> str:
        self.gamer_type = gamer_type

    def set_health(self, health)  -> int:
        self.health = health

    def specification(self)  -> None:
        print(f"Раса - {self.gamer_type}")
        print(f"Жизней {self.health}")

    def update_health(self, enemy_tool_power: int) -> bool:
        self.health = self.health - int(enemy_tool_power)
        self.is_alive()

    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True

    def save_memento(self) -> None:
        """
        Тотем сохраняет состояние.
        """
        print("Сохранено текущее состояние")

        #return Memento(self.health, self.killed_enemies, self.backpack)

    def restore_memento(self) -> None:
        """
        Тотем восстанавливает состояние.
        """
        # self.health = Memento.get_health()
        # self.killed_enemies = Memento.get_killed_enemies()
        # self.backpack = Memento.get_backpack()


class Builder:

    def get_health(self) -> None: pass

    def get_gamer_type(self) -> None: pass

    def get_backpack(self) -> None: pass

    def get_killed_enemies(self) -> None: pass

    def get_is_alive(self) -> None : pass


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
        self.power = random.randint(1, 20)  # сила защиты
        return self.power


class MonsterBuilder(Builder):

    def get_health(self):
        self.health = random.randint(10, 20)
        return self.health

    def update_health(self, hit_power: int) -> int:
        self.health = self.health - hit_power
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
