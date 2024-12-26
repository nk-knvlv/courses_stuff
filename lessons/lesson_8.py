class House:
    term: str
    street: str

    def __init__(self, term, street):
        self.term = term
        self.street = street

    def get_address(self):
        return f"{self.street} - {self.term}"


class Table:
    def __init__(self, w, l, h):
        self.width = w
        self.length = l
        self.height = h


class KitchenTable(Table):
    places: int = 1  # по умолчанию

    def set_places(self, p: int):
        self.places = p


class DeskTable(Table):
    def get_square(self):
        return self.width * self.length


# переопределение родительского метода
class ComputerTable(DeskTable):
    def get_square(self, e):
        return self.width * self.length - e


# расширение родительского метода
class AdminTable(DeskTable):
    def get_square(self, e):
        return DeskTable.get_square(self) - e


# пример использования расширения

# bad
class KitchenTable(Table):
    def __init__(self, w, l, h, p):  # дублирование кода
        self.width = w
        self.length = l
        self.height = h
        self.places = p


# well done
class KitchenTable(Table):
    def __init__(self, w, l, h, p: int):
        Table.__init__(w, l, h)
        self.places = p


class Rectangle:

    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
