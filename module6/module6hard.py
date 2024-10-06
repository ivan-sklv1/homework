class Figure:

    sides_count = 0
    
    def __init__(self, color:list, sides:list, filled=bool):
        self.__color = color
        self.__sides = [sides for i in range(self.sides_count)]
        self.filled = filled
        
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = self.get_color()

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)
    
    def set_sides(self, *args):
        new_list = [*args]
        if self.__is_valid_sides(new_list) is True:
            self.__sides = new_list

class Circle(Figure):

    sides_count = 1
    
    def __init__(self, color: list, sides:int):
        Figure.__init__(self, color, sides)
        self.__radius = 0

    def get_radius(self):
        radius = self.__radius
        

    def get_square(self):
        return self.sides_count / 4 * 3.14


class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        p = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides:list):
        Figure.__init__(self, color, sides)
        self.__sides = sides * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
