from aiohttp.web import Response, View
from app import db
import json
from utilities import validate_data


class HealthView(View):
    """Вью, созданное лишь для возможности проверить жив ли сервис."""

    async def get(self) -> Response:
        """Health-check сервиса."""
        return Response(status=200)


class GetInfo(View):
    async def get(self):
        engine = self.request.app["engine"]
        psq_db = await db.select_data(engine)
        return Response(status=200, body=json.dumps(psq_db))


class InsertInfo(View):
    async def post(self):
        engine = self.request.app["engine"]
        data = await self.request.json()
        if validate_data(data):
            await db.insert_data(data, engine)
            return Response(status=200, body=json.dumps(data))
        else:
            return Response(status=400, text="Невалидный запрос")
