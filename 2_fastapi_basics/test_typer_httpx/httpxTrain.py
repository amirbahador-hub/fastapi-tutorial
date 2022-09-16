import asyncio
import json
import typer
import httpx
from pathlib import Path
from typing import Optional
import pydantic

app = typer.Typer()


class Store(pydantic.BaseModel):
    name: str


class Product(pydantic.BaseModel):
    name: str
    price: int
    store: Optional[Store]


class ReadJson(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.data = json.load(self.file)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


async def readData(path: Path):
    tasks = list()
    with ReadJson(path) as products:
        async with httpx.AsyncClient() as client:
            for product in products:
                tasks.append(asyncio.create_task(
                    writeData(Product(name=product['name'], price=product['price'], store=product['store']))
                ))

            await asyncio.gather(*tasks)


async def writeData(product: Product):
    print(product)


@app.command()
def read(path: Optional[Path] = typer.Option(None)):
    asyncio.run(readData(path=path))


if __name__ == '__main__':
    asyncio.run(app())
