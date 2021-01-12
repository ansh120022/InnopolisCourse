"""Здесь функции для проверок и непосредственно вызов декоратора."""
import re
import jsonschema
from typing import Any
from decorator import valid_all
import random

schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}, "car": {"type": "string"}},
    "required": ["name", "car"],
}


def validate_json(driver_data: dict) -> Any:
    """Валидация входных данных."""
    try:
        bool(jsonschema.validate(driver_data, schema))
        return driver_data
    except jsonschema.ValidationError:
        return False


def check_car_name(driver_data: dict) -> Any:
    """Проверка, что в названии автомобиля только латинские буквы и цифры."""
    regex = "^[A-Z][a-z]*\s[A-z]*\s\d"
    car = driver_data["car"]
    val = random.randint(100, 200)  # для проверки repeat times
    if re.fullmatch(regex, car) or val == 0:
        return driver_data
    else:
        return False


def default_behavior() -> None:
    """Функция, которая выполнится при истечении дозволенного количества повторений."""
    print("Количество попыток валидации истекло.")


@valid_all(
    input_validation=validate_json,
    output_validation=check_car_name,
    on_fail_repeat_times=2,
    default_behavior=default_behavior,
)
def fun(json: dict) -> dict:
    """Валидируемая функция."""
    return json


valid_json = {"name": "Андронников Виталий", "car": "Toyota Camry 8"}

print("\nПроходят все проверки")
print(fun(valid_json))


invalid_json = {"car": 123}

# print("\nНе проходит проверка входных данных")
# print(fun(invalid_json))

invalid_output = {"name": "Андронников Виталий", "car": "<script>attack</>"}

print("\nНе проходит проверка выходных данных")
print(fun(invalid_output))
