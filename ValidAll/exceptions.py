"""Реализация исключений."""


class InputDataError(Exception):
    """Если входные параметры невалидны."""

    def __init__(self, message: str) -> None:
        """Конструктор."""
        self.message = message
        super().__init__(self.message)


class OutputDataError(Exception):
    """Если результат функции невалиден."""

    def __init__(self, message: str = "Результат функции не валиден") -> None:
        """Конструктор."""
        self.message = message
        super().__init__(self.message)

    pass


class RepeatValueError(Exception):
    """Если on_fail_repeat_times = 0."""

    def __init__(self, message: str = "Параметр repeat times не может быть 0") -> None:
        """Конструктор."""
        self.message = message
        super().__init__(self.message)

    pass
