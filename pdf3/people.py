class People:
    def __init__(self) -> None:
        self._name_list = ["Gilad", "Maya", "Ziv", "Yraden", "Shahaf", "Koral", "Matan"]

    def __iter__(self):
        self.curr_index = 0
        return self

    def __next__(self):
        if self.curr_index + 1 >= len(self.name_list):
            del self.curr_index
            raise StopIteration
        self.curr_index += 1
        return self.curr_index

    def add_person(self, name: str) -> None:
        self.name_list.append(name)
