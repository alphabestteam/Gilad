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

if __name__ == "__main__":
    main()