"""Правила игры можно найти в readme.txt."""

import random
from time import sleep
import sys


class Gamer:
    """Класс с атрибутами игрока."""

    def __init__(self, health:int, power:int):
        """Возвращает параметры игрока - здоровье и силу."""
        self.health = health
        self.power = power


class GamerKnight(Gamer):
    """Класс с атрибутами игрока-рыцаря."""

    def __init__(self, health: int, power: int, killed_monsters: int):
        """Возвращает переменную для счётчика побеждённых противников."""
        super(GamerKnight, self).__init__(health, power)
        self.killed_monsters = killed_monsters

    def update_state_after_win(self) -> None:
        """Пересчёт числа здоровья и побеждённых противников после битвы."""
        self.health = self.health - self.power
        self.killed_monsters += 1


monster = Gamer(health=0, power=0)
knight = GamerKnight(health=10, power=10, killed_monsters=0)


def events(event: str, random_health: int, random_power: int)-> None:
    """Запуск нужной функции в зависимости от выпавшего события."""
    if event == 'яблоко':
        event_apple(random_health)
    elif event == 'меч':
        event_sword(random_power)
    else:
        event_fight(random_health, random_power)


def event_apple(random_health: int)-> None:
    """Оповещение пользователя в случае, когда выпало яблочко."""
    knight.health = knight.health + random_health
    print(f"🍏 Ты съел яблоко и получил +{random_health} к здоровью. Cчёт здоровья: {knight.health}")
    sleep(1)


def event_sword(random_power: int)-> None:
    """Выбор пользователя в случае, когда выпал меч."""
    print(f"¤=[]:::::> Это меч с силой {random_power}. Введи 1 - взять этот меч и выбросить старый, 2 - пропустить")
    knight_choice = None
    while knight_choice is None:
        knight_choice = input()
        if knight_choice == '1':
            knight.power = random_power
            break
        elif knight_choice == '2':
            continue
        else:
            knight_choice = None
            print("Ошибка ввода. Введи 1 - взять этот меч и выбросить старый, 2 - пропустить")


def event_fight(random_health: int, random_power: int) -> None:
    """Выбор пользователя в случае, когда выпало сражение."""
    monster.health = random_health
    monster.power = random_power
    print(f"Ты видишь чудовище с силой {monster.power} и здоровьем {monster.health}. Введи 1 - сражаться, 2 - убегать")
    knight_choice = None
    while knight_choice is None or knight.killed_monsters < 10:
        knight_choice = input()
        if knight_choice == '1':
            fight(knight.health)
        elif knight_choice == '2':
            break
        else:
            knight_choice = None
            print("Ошибка ввода. Введи 1 - сражаться, 2 - убегать")


def who_is_stronger(monster_power: int, knight_health: int, knight_power: int, monster_health: int) -> str:
    """Отпределение более более сильного игрока."""
    if monster_power >= knight_health:
        return 'monster'
    if knight_power >= monster_health:
        return 'knight'
    else:
        return 'Error.Try again.'


def fight(knight_health: int) -> int:
    """Определение результата битвы."""
    stronger_gamer = who_is_stronger(monster.power, knight.health, knight.power, monster.health)
    if stronger_gamer == 'monster':
        print("""Поражение. Игра окончена.
             o╮༼ • ̯ • ༽╭o͡͡͡""")
        sys.exit()
    if stronger_gamer == 'knight':
        knight.update_state_after_win()
        if knight_health > 0:
            print(f"Хороший удар! Количество убитых чудовищ - {knight.killed_monsters}")
            if knight.killed_monsters == 10:
                print(""" Победа. Игра окончена
                         ∩༼˵☯‿☯˵༽つ¤=[]:::::>    """)
                sys.exit()
        if knight_health <= 0:
            print("""Поражение. Игра окончена.
                              o╮༼ • ̯ • ༽╭o͡͡͡""")
            sys.exit()
        else:
            generate_random_values()
    return 1


def generate_random_values() -> None:
    """Инициализация случайных значений, запуск игры."""
    while knight.killed_monsters != 10:
        options = ['яблоко', 'меч', 'чудовище']
        event = random.choice(options)
        random_health = random.randint(5, 30)
        random_power = random.randint(5, 30)
        events(event, random_health, random_power)


generate_random_values()
