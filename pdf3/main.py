from people import People


def main():
    people = People()
    for name in people._name_list:
        print(name)


if __name__ == "__main__":
    main()
