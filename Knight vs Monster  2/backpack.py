"""Рюкзак с подобранными магическими предметами."""


class Backpack:
    """Рюкзак с подобранными магическими предметами."""
    def __init__(self, backpack={'Меч': 10}) -> object:
        self.backpack = backpack

    def get_backpack(self) -> dict:
        """Возвращает содержимое рюкзака там, где оно может понядобиться."""
        return self.backpack

    def print_backpack(self) -> None:
        """Печать содержимого рюкзака."""
        print(self.backpack)

    def print_backpack_after_fight(self)-> None:
        """Более подробная печать содержимого рюкзака после битвы."""
        if self.backpack == {}:
            print("После битвы в рюкзаке ничего не осталось")
        else:
            print(f"После битвы у тебя осталось в рюкзаке {self.backpack}")

    def add_to_backpack(self, tool: dict) -> dict:
        """Добавляем в рюкзак подобранное оружие, или заменяем им аналогичное существующее."""
        self.backpack |= tool
        return self.backpack

    def get_available_tools(self) -> dict:
        """Словарь с оружием, доступным для использования в битве в моменте."""
        available_tools = self.get_backpack().copy()
        if 'Лук' not in available_tools.keys() or 'Стрелы' not in available_tools.keys():
            if 'Лук' in available_tools:
                del available_tools['Лук']
            if 'Стрелы' in available_tools:
                del available_tools['Стрелы']
        if 'Тотем' in available_tools.keys():
            del available_tools['Тотем']
        return available_tools

    def update_backpack(self, tool, enemy_health) -> None:
        """
        Обновление содержимого рюкзака после битвы.
        Сила оружия уменьшается на значение кол-ва жизней противника.
        Если сила оружия была потрачена полностью, то оно удаляется из рюкзака.
        """

        for key, value in self.backpack.copy().items():
            if key == tool and value > enemy_health:
                self.backpack[key] = value - enemy_health
            if key == tool and value <= enemy_health:
                del self.backpack[key]
