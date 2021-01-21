from typing import Dict
import sqlalchemy as sa
from app.model import DeliveryStatus

async def insert_data(json_object: Dict, eng):
    """Вставка строчки в табличку.

    Args:
        json_object -- объект в json-виде для вставки в табицу.
        engine -- объект пула подключений к базе.
    """
    table_class = DeliveryStatus
    query_insert = sa.insert(table_class)
    query_insert = query_insert.values(**json_object)
    async with eng.acquire() as conn:
        transaction = await conn.begin()
        try:
            execute_object = await conn.execute(query_insert)
        except Exception as ex:
            await transaction.rollback()
            raise Exception("Will not finish operation with database. {0}".format(ex))
        else:
            await transaction.commit()
            return execute_object


async def select_data(eng):
    """Выборка из таблицы.
        Arg
        eng - engine PG
    """
    table_class = DeliveryStatus
    query_select = sa.select(["*"], use_labels=False).select_from(table_class)
    async with eng.acquire() as conn:
        transaction = await conn.begin()
        try:
            execute_object = await conn.execute(query_select)
            result = await execute_object.fetchall()
            result = [dict(res.items()) for res in result]
        except Exception as ex:
            await transaction.rollback()
            raise Exception("Will not finish operation with database. {0}".format(ex))
        else:
            await transaction.commit()
            return result