from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
class CustomerModel(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    shipping_address = Column(String, nullable=False)

class CartItemModel(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    item_id = Column(Integer)
    quantity = Column(Integer)