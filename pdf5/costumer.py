from product import Product


class Costumer:
    def __init__(self, name: str, shopping_list: list) -> None:
        self._name = name
        self._shopping_list = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def shopping_list(self) -> list:
        return self._shopping_list
    
    def total_price(self) -> int:
        """
        Function that return all the price
        the costumer have to pay
        """
        all_price = 0
        for dict in self.shopping_list:
            all_price += dict["product"].price * dict["units"]
        return all_price

    def add_product(self, product: Product, product_units: int) -> None:
        """
        Function that adds product to the shopping list
        """
        for dict in self.shopping_list:
            if dict["product"].name == product.name:
                dict["units"] += product_units
                return None

        self.shopping_list.append({"product": product, "units": product_units})

    def remove_product(self, product: Product, product_units: int) -> None:
        """
        Function that removes units of product.
        If at the end the units equal 0: 
        the product will be deleted.
        """
        for dict in self.shopping_list:
            if dict["product"].name == product.name:
                dict["units"] -= product_units
                if dict["units"] == 0:
                    self.shopping_list.remove(dict)
                return None
        