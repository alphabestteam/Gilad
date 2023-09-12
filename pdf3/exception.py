def main():
    first_number = input("Enter number: ")
    second_number = input("Enter number: ")
    try:
        print(int(first_number), int(second_number))
    except ValueError:
        print("Invalid input")

    print("Finished running")


if __name__ == "__main__":
    main()
