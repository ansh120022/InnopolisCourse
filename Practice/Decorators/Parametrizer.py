from typing import Callable, Any

def my_parametrizer(x: str, y: list) -> Callable:
    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("то что происходит ДО вызова функции")

            for i in y:
                kwargs[x] = i
                result = func(*args, **kwargs)

            print("то что происходит ПОСЛЕ вызова функции")
            return result

        return wrapper

    return decoration


@my_parametrizer('x', [1, 2, 3, 8, 9, 10])

def test_x_lt_10(x):
    assert x < 10
    print('тест для значения', x, 'успешен')

test_x_lt_10()
