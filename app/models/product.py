from sqlalchemy import Column, Integer, String, Float
from app.database.db import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String)
    category_id = Column(Integer)
    category_name = Column(String)

    department_id = Column(Integer)
    department_name = Column(String)

    product_price = Column(Float)