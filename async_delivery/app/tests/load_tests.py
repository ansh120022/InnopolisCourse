"""
Тесты на нагрузку.

Запуск locust -f load_tests.py --host=http://localhost:8081
"""
from typing import Any
from locust import HttpUser, task, between
import random
import json

status_list = ["Обрабатывается", "Выполняется", "Доставлено"]


def generate_test_data() -> Any:
    """Генерация тела запроса."""
    data = {
        "order_id": "id"+str(random.randint(1, 999)),
        "delivery_status": random.choice(status_list)
    }
    return (json.dumps(data, ensure_ascii=False))


class IndexLoading(HttpUser):
    """Создание клиента."""

    wait_time = between(2, 5)

    @task
    def status_page(self: Any) -> None:
        """GET-запрос."""
        self.client.get("/status")

    @task
    def add_page(self: Any) -> None:
        """POST-запрос."""
        data = generate_test_data()
        self.client.post("/add", data.encode('utf-8'))
