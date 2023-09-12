import random


class Product:
    def __init__(self, name: str) -> None:
        self._name = name
        self._price = random.randint(1,5)

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price

    