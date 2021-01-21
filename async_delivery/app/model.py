from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import config


Base = declarative_base()
metadata = Base.metadata


class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    order_id = Column(
        String,
        primary_key=True,
        comment="Идентификатор."
    )

    delivery_status = Column(
        String,
        comment="Статус доставки."
    )


engine = create_engine(config.ENGINE_STRING)
Base.metadata.create_all(engine)
del engine


