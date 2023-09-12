import random

name_list = [
    "Yael",
    "Avner",
    "Malka",
    "Oryan",
    "Yonatan",
    "Iftach",
    "Eviatar",
    "Gilad",
    "Roni",
    "Ori",
]
age_list = [61, 59, 32, 31, 29, 28, 25, 19, 9, 4]
id_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


class Person:
    def __init__(self):
        self.name = random.choice(name_list)
        self.id = random.choice(id_list)
        id_list.remove(self.id)
        self.age = random.choice(age_list)

    def __str__(self) -> str:
        return f"hi {self.name}"

    # Getter method for the name attribute
    def get_name(self):
        return self.name

    # Getter method for the id attribute
    def get_id(self):
        return self.id

    # Getter method for the age attribute
    def get_age(self):
        return self.age

    # Setter method for the name attribute
    def set_name(self, name):
        self.name = name

    # Setter method for the id attribute
    def set_id(self, id):
        self.id = id

    # Setter method for the age attribute
    def set_age(self, age):
        self.age = age

    # Function that print the attribute of the class Person
    def print_person(self) -> str:
        print(
            f"The name of the person is {self.name}\nThe id of the person is {self.id}\nThe age of the person is {self.age}"
        )
