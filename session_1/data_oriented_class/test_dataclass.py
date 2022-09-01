import json
from dataclasses import dataclass
from typing import Optional

#class Product:

#    def __init__(self, name: str, price:int, _id:int):
#        self.name =  name
#        self.price=  price

#    def __str__(self):
#        return self.name self._id

@dataclass
class Product:
    price:int
    name: str
    discounted_price: Optional[int]



def main() -> None:
    with open("data.json") as file:
        data = json.load(file)
        for product in data:
            #print(product["name"])
            p = Product(name=product["name"], price=product["basePrice"], discounted_price=product["discountedPrice"])
            print(p)


if __name__ == "__main__":
    main()
