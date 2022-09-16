import pydantic
import json
from typing import Optional, List

class NumberGtZeroError(Exception):
    def __init__(self, value:str, message:str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class Product(pydantic.BaseModel):
    name: str
    _id: str
    basePrice: int
    images: list[str]
    discountedPrice: Optional[int] = 0

    @pydantic.validator("basePrice")
    @classmethod
    def base_price_valid(cls, value):
        if value < 0:
            raise NumberGtZeroError(value=value, message="Price should be greater than 0")
        return value


def main() -> None:

    with open("data.json") as file:
        data = json.load(file)
        products: List[Product] = [Product(**p) for p in data]
        print(products[3].basePrice)

            #print(product["name"])
            #p = Product(name=product["name"], price=product["basePrice"], discounted_price=product["discountedPrice"])
            #print(p)


if __name__ == "__main__":
    main()
