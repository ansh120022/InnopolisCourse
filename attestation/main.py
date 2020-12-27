import pprint
import itertools
from typing import Iterable, Dict, Optional, List, Any
from itertools import product

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
        "ресурс": "неарабика",
        "тип": "кофе",
        "количество": 2000,
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
    conveyor_resource = itertools.groupby(available_ingredients_list, get_resource)
    coffee_beans_we_have = list() #виды кофе
    water_we_have = list() #Виды воды
    milk_we_have = list()  #Виды молока
    syrups_we_have = list() #Виды сиропов
    instructions = list()  # все инструкции
    for key, group in conveyor_resource:
        for resource in group:
            if resource.get("тип") == "кофе" and resource.get('количество') > resource.get('порция'):
                coffee_beans_we_have.append({resource.get("тип"): resource.get("ресурс")})
            if resource.get("тип") == "вода" and resource.get('количество') > resource.get('порция'):
                water_we_have.append({resource.get("тип"): resource.get("ресурс")})
            if resource.get("тип") == "молоко" and resource.get('количество') > resource.get('порция'):
                milk_we_have.append({resource.get("тип"): resource.get("ресурс")})
            if resource.get("тип") == "сироп" and resource.get('количество') > resource.get('порция'):
                syrups_we_have.append({resource.get("тип"): resource.get("ресурс")})

    pure_coffee = list(itertools.product(coffee_beans_we_have, water_we_have)) #Инструкции по созданию кофе без добавок
    instructions.append(pure_coffee)
    white_coffee = list(itertools.product(pure_coffee, milk_we_have))  # Инструкции по созданию кофе c молоком
    instructions.append(white_coffee)
    pure_coffee_with_syrup = list(itertools.product(pure_coffee, syrups_we_have))
    instructions.append(pure_coffee_with_syrup)
    white_coffee_with_syrup = list(itertools.product(pure_coffee, syrups_we_have))
    instructions.append(white_coffee_with_syrup)

    print(instructions[0])

    return instructions


#pp.pprint(calculate(available_ingredients))
calculate(available_ingredients)



