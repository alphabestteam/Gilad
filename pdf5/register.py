from costumer import Costumer


class Register:
    def __init__(self) -> None:
        self._register_sum = 0
        self._register_list = []

    @property
    def register_sum(self) -> int:
        return self._register_sum

    @property
    def register_list(self) -> list:
        return self._register_list

    @register_sum.setter
    def register_sum(self, register_sum_add: int) -> None:
        self._register_sum += register_sum_add

    @register_list.setter
    def register_list(self, new_register_list: list) -> None:
        self._register_list = new_register_list

    def checkout_costumer(self, costumer: Costumer) -> None:
        """
        Function that received costumer
        and add the total sum of the costumer to the
        register sum.
        """
        self.register_sum += costumer.total_price()
        self.register_list.append(
            {"name": costumer.name, "price": costumer.total_price()}
        )

    def print_summery(self) -> str:
        """
        Function that print the profit sum
        and the sales list of the register
        """
        print(f"The profit sum of the cash register is: {self.register_sum}")
        print(f"The sales list of the cash register is: {self.register_list}")
