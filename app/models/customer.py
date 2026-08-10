from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)

    customer_segment = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zipcode = Column(Integer)