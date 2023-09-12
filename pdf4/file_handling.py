def main():
    file_path = "pdf4\\file_handling_text.txt"

    with open(file_path, "r") as file:
        print(file.read())

    with open(file_path, "w") as file:
        file.write("My name is Gilad")

if __name__ == "__main__":
    main()
