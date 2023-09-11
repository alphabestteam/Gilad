import random


def addition(first_number=0, second_number=0) -> int:
    return first_number + second_number


def hii_name(name: str) -> str:
    print(f"Hello {name}! Great to see u")


def quadratic_equation(a_number: int, b_number: int, c_number: int) -> int:
    root = (b_number**2) - (4 * a_number * c_number)

    if root > 0:
        first_result = (-b_number + (root**0.5)) / (2 * a_number)
        second_result = (-b_number - (root**0.5)) / (2 * a_number)
        return first_result, second_result
    else:
        print("roots are imaginary")


def random_number(first_number: float or int, second_number: float or int) -> int:
    if type(first_number) and type(second_number) == float:
        return random.randint(first_number, second_number)
    elif type(first_number) and type(second_number) == int:
        return random.randint(first_number, second_number)


def main():
    addition(5,2)
    hii_name("Gilad")
    quadratic_equation(1,2,3)
    random_number(4,4)


if __name__ == "__main__":
    main()
