"""Правила валидации пользовательского ввода."""

def valid_input(user_input: str) -> bool:
    """
    Так как по правилам игры пользователь использует цифры для управления,
    то проверяем пользовательский ввод на то, что это действительно число.
    """
    try:
        int(user_input)
    except ValueError:
        print("Ошибка ввода")
        return False
    else:
        return True
