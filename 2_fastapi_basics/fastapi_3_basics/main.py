import sqlalchemy
import databases
from fastapi import FastAPI, Request
from pydantic import BaseModel


DATABASE_URL = "postgresql://fastapi_test_user:fastapi_test_password@localhost:5432/fastapi_test_db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table(
        "books",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("price", sqlalchemy.Integer),
        sqlalchemy.Column("discounted_price", sqlalchemy.Integer),
        )


app = FastAPI()

class Product(BaseModel):
    name:  str
    price: int
    discounted_price: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/products/")
async def create_product(product_data: Product):
    data = product_data.dict()
    query = products.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.get("/products/")
async def get_all_products():
    query = products.select()
    return await database.fetch_all(query)
