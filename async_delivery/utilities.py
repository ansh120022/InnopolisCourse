"""Дополнительные функции."""
import re
import jsonschema

regex = "[a-z0-9]{2,5}"
status_list = ["Обрабатывается", "Выполняется", "Доставлено"]

schema = {
  "type": "object",
  "properties": {
    "order_id": {
      "type": "string"
    },
    "delivery_status": {
      "type": "string"
    }
  },
  "required": [
    "order_id",
    "delivery_status"
  ]
}


def validate_data(data):
    if validate_json(data):
        if validate_input(data["order_id"], data["delivery_status"]):
            return True
    else:
        return False


def validate_input(d_id: str, d_status: str) -> bool:
    """Проверка требований к значениям полей."""
    if 2 <= len(d_id) <= 5:
        if not re.match(regex, d_id):
            return False
        else:
            if d_status in status_list:
                return True
            else:
                return False
    else:
        return False


def validate_json(input_json: dict) -> bool:
    """Валидация по схеме."""
    try:
        jsonschema.validate(input_json, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False