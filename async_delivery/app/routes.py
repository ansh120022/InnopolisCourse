from aiohttp import web

from app.views import HealthView, GetInfo, InsertInfo


def inject_routes(app: web.Application) -> None:
    """Инициализация роутов."""
    app.add_routes(
        [
            web.view("/heartbeat", HealthView),
            web.view("/add", InsertInfo),
            web.view("/status", GetInfo)
        ]
    )
