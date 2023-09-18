N = 10


def function(N: int) -> str:
    first_number = 1
    second_number = 2
    yield first_number
    second_number
    for _ in range(3, N):
        new_number = first_number * second_number
        second_number = first_number
        first_number = new_number
        yield new_number


def main():
    for number in function(N):
        print(number)


if __name__ == "__main__":
    main()
