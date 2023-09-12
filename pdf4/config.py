import configparser


def main():
    config = configparser.ConfigParser()
    config.add_section("header")
    config.set("header", "data", "hi")
    config.set("header", "silent", "True")

    with open("config.ini", "w") as file:
        config.write(file)

    config.read("config.ini")
    data = config.get("header", "data")
    uppercase_string = data.upper()

    if config.get("header", "silent") == "True":
        print(config.get("header", "data"))

    config.set("header", "data", uppercase_string)


if __name__ == "__main__":
    main()
