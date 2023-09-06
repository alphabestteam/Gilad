def prime_number(number: int) -> str:
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
    if flag:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


def main():
    sum = 0
    for i in range(1,100):
        sum += i
    # return sum
    
    prime_number(5)
    prime_number(6)
    prime_number(7)
    prime_number(14)
    prime_number(152)
    prime_number(60693)

if __name__ == "__main__":
    main()