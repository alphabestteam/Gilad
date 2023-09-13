from point import Point


def main():
    first_obj = Point(4, 6)
    second_obj = Point(4, 6)
    print(first_obj == second_obj)
    print(first_obj, second_obj)
    print(first_obj + second_obj)

if __name__ == "__main__":
    main()