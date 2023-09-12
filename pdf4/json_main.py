import json


def main():
    with open("pdf4\json_file.json", "r") as file:
        loaded_data = json.load(file)

    print((loaded_data))

    loaded_data["human"][0]["name"] = "Gilad"
    loaded_data["human"][0]["age"] = 19
    loaded_data["human"][0]["city"] = "Ashkelon"

    with open("new_json_file.json", "w") as new_file:
        json.dump(loaded_data, new_file)


if __name__ == "__main__":
    main()
