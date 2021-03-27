# """хранение состояния игрока."""
#
#
# class Memento:
#
#     def __init__(self, backpack: dict, health: int, killed_enemies: int):
#         self.backpack = backpack
#         self.health = health
#         self.killed_enemies = killed_enemies
#
#     def get_health(self) -> int:
#         return self.health
#
#     def get_backpack(self) -> dict:
#         """
#         Создатель использует этот метод, когда восстанавливает своё состояние.
#         """
#         return self.backpack
#
#     def get_killed_enemies(self) -> int:
#         """
#         Создатель использует этот метод, когда восстанавливает своё состояние.
#         """
#         return self.killed_enemies
