from math import pi, pow, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        if len(sides) != self.sides_count:
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            self.__sides = list(sides)
        self.filled = True

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(rgb):
        return all(0 <= value <= 255 for value in rgb)

    def set_color(self, *args):
        if self.__is_valid_color(args):
            self.__color = list(args)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_radius(self):
        return self.__radius()

    def get_square(self):
        if isinstance(self, Circle):
            return pi * pow(self.__radius(), 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        if isinstance(self, Triangle):
            p = self.__len__() / 2
            return sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides_list = [sides[0] for _ in range(self.sides_count)]
            super().__init__(color, *sides_list)
        elif len(sides) == self.sides_count and all(x == sides[0] for x in sides) is False:
            sides_list = [max(sides) for _ in range(self.sides_count)]
            super().__init__(color, *sides_list)
        else:
            super().__init__(color, *sides)

    def get_volume(self):
        return int(pow(self.get_sides()[0], 3))


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится

print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
