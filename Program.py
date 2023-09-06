def prime_number(number: int) -> str:
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
    if flag:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


def assembly_of_number(number: int) -> int:
    multipication = 1
    for i in range(1,number):
        multipication *= i
    return multipication


def main():
    sum = 0
    for i in range(1,100):
        sum += i
    print(assembly_of_number(5))
    print(assembly_of_number(6))
    print(assembly_of_number(7))
    print(assembly_of_number(8))
    print(prime_number(5))
    print(prime_number(6))
    print(prime_number(7))
    print(prime_number(14))
    print(prime_number(152))
    print(prime_number(60693))

if __name__ == "__main__":
    main()