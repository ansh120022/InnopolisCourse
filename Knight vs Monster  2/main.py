"""В этом файле реализован паттерн Стратегия и основной функционал игры."""

from __future__ import annotations

import sys
from gamers_builder import Director, HeroBuilder, MonsterBuilder
import random
from time import sleep
from magic_tools_factory import generate_magic_tool
from abc import ABC, abstractmethod
from validation import valid_input

GamerBuilder = HeroBuilder()
director = Director()

director.set_builder(HeroBuilder)
Hero = director.get_gamer()
print("Создан герой c параметрами:")
Hero.specification()
print("В рюкзаке у героя:")
Hero.backpack.print_backpack()
print("\nНачало игры.............\n")


def save_memento():
    """Заглушка."""
    return 0


def restore_memento()-> None:
    """Заглушка."""
    return 0


def event_apple(apple_power) -> None:
    """Пересчёт здоровья и оповещение пользователя в случае, когда выпало яблочко."""
    Hero.health += apple_power
    print(f"Ты съел яблочко и получил + {apple_power} на счёт жизней. Теперь у тебя жизней: {Hero.health}")
    sleep(1)


def choose_tool_to_fight() -> tuple:
    """Пользователь выбирает оружие для удара."""
    available_tools = Hero.backpack.get_available_tools()
    if available_tools != {}:
        print("Для атаки доступно оружие:")
        for i, (key, value) in enumerate(available_tools.items()):
            print(f"{i} - {key} c силой {value}")
            i = i + 1
        user_choice = input("Твой выбор:\n")
        for i, (key, value) in enumerate(available_tools.items()):
            if i == int(user_choice):
                return (key, value)
    else:
        return ("Оружия нет")


# ---------------------------------------------- Стратегия -----------------------------------------------#


class Context():
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов.
    """
    def __init__(self, strategy: Strategy) -> None:
        """
        Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Контекст хранит ссылку на один из объектов Стратегии.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Контекст позволяет заменить объект Стратегии во время выполнения.
        """
        self._strategy = strategy

    def do_some_business_logic(self, monster_power) -> None:
        """
        Контекст делегирует некоторую работу объекту Стратегии.
        """
        self._strategy.do_algorithm(monster_power)


class Strategy(ABC):
    """Абстрактная стратегия."""

    @abstractmethod
    def do_algorithm(self) -> None:
        """Абстрактный метод для всех стратегий."""
        pass


"""
Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""


class Fight(Strategy):
    """Конкретная стратегия Сражаться."""

    def do_algorithm(self, monster_power) -> None:
        """Конкретная стратегия Сражаться."""
        print("Началась битва")
        print("<:::::[]=¤ Монстр нанёс удар")
        sleep(1)
        print("Ты нанёс удар ¤=[]:::::>")
        sleep(1)
        Hero.update_health(monster_power)


class Defense(Strategy):
    """Конкретная стратгия Защищаться."""

    def do_algorithm(self, monster_power) -> None:
        """Конкретная стратгия Защищаться."""
        print("<:::::[]=¤ Монстр нанёс удар")
        sleep(1)
        print(f"Использована защита типа {Hero.gamer_type} c силой {Hero.power}")
        sleep(1)
        if Hero.power < monster_power:
            monster_power = monster_power - Hero.power
        else:
            monster_power = 0
        print("Ты нанёс удар ¤=[]:::::>")
        sleep(1)
        Hero.update_health(monster_power)


class Ignore(Strategy):
    """Конкретная стратгия Пройти мимо."""

    def do_algorithm(self, monster_power) -> None:
        """Конкретная стратгия Пройти мимо."""
        print("....Да, в другой раз....\n")
        sleep(1)


class RestoreSnapshot(Strategy):
    """Конкретная стратгия восстановления сохранённого состояния из тотема."""

    def do_algorithm(self, monster_power) -> int:
        """Общая функция."""
        #Hero.backpack = Memento.get_backpack()
        Hero.specification()
        return 0


# ------------------------------------------Конец стратегии ------------------------------------#

def generate_random_events() -> None:
    """Инициализация случайных событий и то, что происходит с каждым событием."""
    while Hero.killed_enemies <= 10 and Hero.is_alive():
        options = ['Магический предмет', 'Монстр']
        event = random.choice(options)
        if event == 'Магический предмет':
            tool = generate_magic_tool()
            if 'Яблочко' in tool:
                apple_power = tool['Яблочко']
                event_apple(apple_power)
                continue
            b = input(f"\nТы видишь {tool}\n 1 - Взять, 2 - Пройти мимо\n")
            if valid_input(b):
                if b == '1' and 'Тотем' in tool:
                    # Hero.save_memento()
                    save_memento()
                    sleep(1)
                    Hero.backpack.add_to_backpack({"Тотем": 1})
                    continue
                if b == '1':
                    Hero.backpack.add_to_backpack(tool)
                    print("Теперь в рюкзаке:")
                    Hero.backpack.print_backpack()
                    print("--------------------------------------------\n")
                    sleep(1)
                else:
                    context = Context(Ignore())
                    context.do_some_business_logic(b)
        else:
            Monster = generateMonster()
            print(f"\nТы видишь монстра с силой {Monster.power}")
            Monster.specification()
            b = input("\n 1 - Сражаться, 2 - Пройти мимо\n")
            while not valid_input(b):
                b = input("\n 1 - Сражаться, 2 - Пройти мимо\n")
            if valid_input(b):
                if b == '1':
                    # Пока монстр и герой живы и у героя ещё есть инструменты продолжаем битву
                    while Monster.is_alive() and Hero.is_alive():
                        chosen_tool = ()
                        chosen_tool = choose_tool_to_fight()
                        if chosen_tool == 'Оружия нет':
                            print("""Но у тебя нет оружия. Игра окончена.
                                                                                  o╮༼ • ̯ • ༽╭o͡͡͡""")
                            if 'Тотем' in Hero.backpack.get_backpack():
                                b = input("У тебя есть тотем. Использовать его? 1 - Да, 2 - Нет\n")
                                if valid_input(b):
                                    if b == '1':
                                        # context = Context(RestoreSnapshot())
                                        # context.do_some_business_logic('f')
                                        restore_memento()
                            else:
                                sys.exit()
                            continue
                        if Hero.gamer_type == Monster.gamer_type:
                            context = Context(Defense())
                            context.do_some_business_logic(Monster.power)
                        else:
                            context = Context(Fight())
                            context.do_some_business_logic(Monster.power)
                        Hero.backpack.update_backpack(chosen_tool[0], Monster.health)
                        Monster.update_health(chosen_tool[1])
                        if Monster.is_alive():
                            print(f"Монстр всё ещё жив, у него осталось жизней: {Monster.health}\t")
                            print("Нужно продолжать битву!\n")
                            sleep(1)
                        if not Hero.is_alive():
                            print("""У тебя закончились жизни. Игра окончена.
                                                          o╮༼ • ̯ • ༽╭o͡͡͡""")
                            if 'Тотем' in Hero.backpack.get_backpack():
                                b = input("У тебя есть тотем. Использовать его и продолжить игру? 1 - Да, 2 - Нет\n")
                                if valid_input(b):
                                    if b == 1:
                                        restore_memento()
                            else:
                                sys.exit()
                        if not Monster.is_alive():
                            Hero.count_killed_enemies()
                            print(f"Хороший удар! Количество убитых монстров: {Hero.killed_enemies}\n")
                            sleep(1)
                            Hero.backpack.print_backpack_after_fight()
                            sleep(1)
                            print(f"Осталось жизней: {Hero.health}")
                            sleep(1)
                            print("Игра продолжается")
                            sleep(1)
                else:
                    context = Context(Ignore())
                    context.do_some_business_logic('f')
                    continue
    if Hero.killed_enemies >= 10:
        print(""" Победа. Игра окончена
                                 ∩༼˵☯‿☯˵༽つ¤=[]:::::>    """)
        sys.exit()


def generateMonster() -> object:
    """Создание монстра."""
    director.set_builder(MonsterBuilder)
    Monster = director.get_gamer()
    return Monster


generate_random_events()
