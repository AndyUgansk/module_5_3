class House:
    # Определяем метод __init__ для инициализации объекта
    def __init__(self, name, number_of_floors):
        # Установка атрибута self.name с помощью переданного значения name
        self.name = name
        # Установка атрибута self.number_of_floors с помощью переданного значения number_of_floors
        self.number_of_floors = number_of_floors

    def __str__(self):
        # Метод __str__ возвращает строковое представление здания в указанном формате
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Метод для сравнения на равенство числа этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    # Метод для сравнения этажей <
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    # Метод для сравнения этажей <=
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    # Метод для сравнения этажей >
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    # Метод для сравнения этажей >=
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Метод для сравнения этажей !=
    def __ne__(self, other):
        return not self.__eq__(other)

    # Метод для увеличения числа этажей
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Метод для правого сложения
    def __radd__(self, value):
        return self.__add__(value)

    # Метод для сложения с присваиванием
    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(str(h1))
print(str(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
