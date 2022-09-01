from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional

class ProductStatus(Enum):
    published = "published"
    pending = "pending"
    deleted  = "deleted"

class ProductPicture(SQLModel, table=True):
    id: Field(primary_key=True)
    url: str
    product: int = Field(default=..., foreign_key='product.id')

class Product(SQLModel, table=True):
    id: Field(primary_key=True)
    name: str
    status: Optional[ProductStatus] = "published"
    price: int
    discounted_price: Optional[int] = 0 
