from typing import Callable, Any

validate_input_x = lambda x: x != 0

def my_validator(x: str, y:Callable) -> Callable:
    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if y (kwargs.get(x)):
                return func(*args, **kwargs)
        return wrapper

    return decoration


@my_validator('b', validate_input_x)
def div(a, b):
    result = a / b
    return result

print(div(a=6, b=3))


