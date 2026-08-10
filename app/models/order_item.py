from sqlalchemy import Column, Integer, Float
from app.database.db import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)

    quantity = Column(Integer)

    product_price = Column(Float)

    discount = Column(Float)
    discount_rate = Column(Float)

    sales = Column(Float)
    total = Column(Float)

    profit_ratio = Column(Float)
    profit_per_order = Column(Float)

    benefit_per_order = Column(Float)