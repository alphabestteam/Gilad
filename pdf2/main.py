def words_length(*args) -> str:
    """
    Function that receives some parameters that the user wants,
    and print the sum of the received word lengths.
    """
    sum = ""
    for word in args:
        sum += word
    print(sum)


def total_age(**kwargs) -> str:
    """
    Function that print the names of the ages
    and the value attributed to the son.
    """
    ages_sum = 0
    for key in kwargs.keys():
        print(f"The name of the age: {key}. The age: {kwargs[key]}")
        ages_sum += kwargs[key]
    print(f"The sum of the ages is: {ages_sum}")


def main():
    words_length("hii", "Gilad")
    total_age(age1=10, age2=20, age3=30)


if __name__ == "__main__":
    main()
