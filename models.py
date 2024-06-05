from typing import Optional
from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    first_name: str
    second_name: str
    phone: int
    email: str
    password: str
    address: str
    
class Food(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    price: int
    
class Order(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    customer_id: Optional[int] = Field(foreign_key='customer.id',
                                   default=None)
    food_id: Optional[int] = Field(foreign_key='food.id',
                                   default=None)
    count: int
    sum: int
    status: str
    delivery_address: str
    payment: str
    order_time: str
    
class Order_Payment(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    order_id: Optional[int] = Field(foreign_key='order.id',
                                   default=None)
    sum: str
    payment_method: str
    payment_date: str
    
class Delivery(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    customer_id: Optional[int] = Field(foreign_key='customer.id',
                                   default=None)
    order_id: Optional[int] = Field(foreign_key='order.id',
                                   default=None)
    phone: int
    address: str