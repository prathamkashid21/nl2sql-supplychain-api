from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database.db import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, index=True)

    order_date = Column(DateTime)

    order_status = Column(String)

    market = Column(String)

    order_city = Column(String)
    order_state = Column(String)
    order_country = Column(String)
    order_region = Column(String)

    shipping_mode = Column(String)

    shipping_date = Column(DateTime)

    days_for_shipping_real = Column(Integer)
    days_for_shipment_scheduled = Column(Integer)

    delivery_status = Column(String)
    late_delivery_risk = Column(Integer)

    order_zipcode = Column(Float)