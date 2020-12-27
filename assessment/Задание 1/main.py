import pprint
import itertools
from typing import Dict, Optional, List, Any

pp = pprint.PrettyPrinter(indent=4)

ready_to_drink = {}

available_ingredients = [
    {
        "ресурс": "арабика",
        "тип": "кофе",
        "количество": 1000,
        "порция": 10
    },
    {
        "ресурс": "неАрабика",
        "тип": "кофе",
        "количество": 1000,
        "порция": 10
    },
    {
        "ресурс": "молоко",
        "тип": "молоко",
        "количество": 1000,
        "порция": 60
    },
    {
        "ресурс": "вода",
        "тип": "вода",
        "количество": 1000,
        "порция": 60
    },
    {
        "ресурс": "карамель",
        "тип": "сироп",
        "количество": 700,
        "порция": 80
    },
    {
            "ресурс": "миндаль",
            "тип": "сироп",
            "количество": 500,
            "порция": 80
        },
]


class OutOfResourceError(Exception):
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


def get_resource(item: Dict) -> Optional[int]:
    return item.get("тип")


def calculate(available_ingredients_list: list) -> List:
    ingredients = itertools.groupby(available_ingredients_list, get_resource)
    coffee_beans_we_have = {}  # виды кофе
    water_we_have = {}  # Виды воды
    milk_we_have = {}  # Виды молока
    syrups_we_have = {}  # Виды сиропов
    instructions = list()  # все инструкции
    for key, group in ingredients:
        for resource in group:
            if resource.get("тип") == "кофе" and (resource.get('количество') // resource.get('порция')) >= 1:
                coffee_beans_we_have[resource.get("ресурс")] = "кофе"
            if resource.get("тип") == "вода" and (resource.get('количество') // resource.get('порция')) >= 1:
                water_we_have[resource.get("ресурс")] = "вода"
            if resource.get("тип") == "молоко" and (resource.get('количество') // resource.get('порция')) >= 1:
                milk_we_have[resource.get("ресурс")] = "молоко"
            if resource.get("тип") == "сироп" and (resource.get('количество') // resource.get('порция')) >= 1:
                syrups_we_have[resource.get("ресурс")] = "сироп"

    # Инструкции по созданию кофе без добавок
    dark_coffee = list(itertools.product(coffee_beans_we_have, water_we_have))
    instructions.append(dark_coffee)
    # Инструкции по созданию кофе c молоком
    white_coffee = list(itertools.product(dark_coffee, milk_we_have))
    instructions.append(white_coffee)
    # Инструкции по созданию кофе c сиропом
    dark_coffee_with_syrup = list(itertools.product(dark_coffee, syrups_we_have))
    instructions.append(dark_coffee_with_syrup)
    # Инструкции по созданию кофе c молоком сиропом
    white_coffee_with_syrup = list(itertools.product(white_coffee, syrups_we_have))
    instructions.append(white_coffee_with_syrup)

    if not any(instructions):
        raise OutOfResourceError("Всё закончилось")

    return instructions




pp.pprint(calculate(available_ingredients))



