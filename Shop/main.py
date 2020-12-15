"""Валидация полученного json через схему и запись в базу."""

import jsonschema
import psycopg2
import json
from config import config


def read_json(file: str) -> dict:
    """Чтение из файла в словарь."""
    with open(file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


input_json = read_json("input_data.json")
validation_schema = read_json("goods_schema.json")


def validate(file: dict, schema: dict) -> bool:
    """Валидация входного файля через схему."""
    try:
        jsonschema.validate(file, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False


def prepare_tuple(input_dict: dict) -> tuple:

    """Убирает вложенность и формирует кортежи для последующей записи в БД.
    Для каждой таблицы создаётся отдельный кортеж.
    """
    goods = []
    shops_goods = []
    for key, value in input_dict.items():
        if key == "id":
            goods.append(value)
            shops_goods.append(value)
        if key == "name":
            goods.append(value)
        if isinstance(value, dict):
            sub_element = value
            for sub_key, sub_value in sub_element.items():
                if sub_key == "width":
                    goods.append(sub_value)
                if sub_key == "height":
                    goods.append(sub_value)
        if isinstance(value, list):
            for i in range(len(value)):
                sub_element = value[i]
                for sub_key, sub_value in sub_element.items():
                    if sub_key == "location":
                        shops_goods.append(sub_value)
                    if sub_key == "amount":
                        shops_goods.append(sub_value)
    return tuple(goods), tuple(shops_goods)


goods_list, shops_list = prepare_tuple(input_json)


create_query = '''create table if not exists goods 
                        (id int unique not null primary key, name varchar not null, 
                        package_height float not null, package_width float not null);
                        create table if not exists shops_goods 
                        (id serial not null, id_good int unique not null references goods (id) unique, 
                        location varchar not null, amount int not null);
                        
                        COMMENT on column goods.id IS 'уникальный идентификатор товара';
                        COMMENT on column goods.name IS 'аименование товара';
                        COMMENT on column goods.package_height IS 'высота упакованного товара';
                        COMMENT on column goods.package_width IS 'ширина упакованного товара';
                        COMMENT on column shops_goods.id IS 'идентификатор записи';
                        COMMENT on column shops_goods.id_good IS 'идентификатор товара';
                        COMMENT on column shops_goods.location IS 'адрес магазина';
                        COMMENT on column shops_goods.amount is 'количество этого товара в этом магазине';'''

add_goods_query = f"""Insert into goods (id, name, package_width, package_height) 
                        values {goods_list}
                        ON CONFLICT(id) do update
                        set 
                        name = excluded.name, 
                        package_width = excluded.package_width, 
                        package_height = excluded.package_height;"""

add_shops_query = f"""Insert into shops_goods (id_good, location, amount) values {shops_list}
                    ON CONFLICT(id_good) do update
                    set 
                    location = excluded.location, 
                    amount = excluded.amount;"""


def write_db() -> str:
    """Подключение к БД и выполнение запросов."""
    conn = None
    try:
        params = config()
        print('Подключение к базе данных...')
        conn = psycopg2.connect(**params)
        db_cursor = conn.cursor()
        print('Выполнение запроса...')
        db_cursor.execute(create_query)
        db_cursor.execute(add_goods_query)
        db_cursor.execute(add_shops_query)
        print('Запрос выполнен успешно.')
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Соединение закрыто.')
    return 'Success'


def main() -> str:
    """Проверка валидации, запись в БД."""
    if validate(input_json, validation_schema):
        write_db()
        return 'Success'
    else:
        print("Входной json-файл не валиден")
        return 'non valid json'


main()
