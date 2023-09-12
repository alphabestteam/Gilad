from product import Product
from costumer import Costumer
from register import Register


def main():
    first_costumer = Costumer("Gilad", [])
    first_costumer.add_product(Product("Banana"), 5)
    first_costumer.remove_product(Product("Banana"), 2)
    first_register = Register()
    first_register.checkout_costumer(first_costumer)
    first_register.print_summery()
    second_register = Register()


if __name__ == "__main__":
    main()
