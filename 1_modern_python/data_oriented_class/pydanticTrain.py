import pydantic
from typing import Optional, List
import json


class MinesNumberError(Exception):
    def __init__(self, value: str, messages: str = "") -> None:
        self.value = value
        self.messages = messages
        super().__init__(messages)


class Store(pydantic.BaseModel):
    name: str
    store_address: str
    lat: Optional[str]
    lon: Optional[str]
    description: Optional[str]


class Product(pydantic.BaseModel):
    id: str
    name: str
    basePrice: int
    category: str
    discountedPrice: Optional[int]
    images: List[str]
    store: Optional[Store]

    @pydantic.validator("basePrice")
    @classmethod
    def validBasePrice(cls, value) -> int:
        if value < 200:
            raise MinesNumberError("base price less than zero")
        return value


class ReadJson(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.data = json.load(self.file)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def main() -> None:
    products = []
    with ReadJson("data.json") as data:
        for product in data:
            products.append(
                Product(id=product["_id"], name=product["name"],
                        basePrice=product["basePrice"], discountedPrice=product["discountedPrice"],
                        category=product["category"], images=product["images"],
                        store=product["store"]
                        )
            )

    for product in products:
        print(product)


if __name__ == "__main__":
    main()
