# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
# для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі
# порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area_of_figure(self):
        pass

    @abstractmethod
    def perimeter_of_figure(self):
        pass


class Rectangle(Figure):
    def __init__(self, side_length, side_width):
        self.__side_length = side_length
        self.__side_width = side_width

    def area_of_figure(self):
        return self.__side_length * self.__side_width

    def perimeter_of_figure(self):
        return 2 * self.__side_length + 2 * self.__side_width


class Triangle(Figure):
    def __init__(self, triangle_base, triangle_height, side_length_a, side_length_b):
        self.__triangle_base = triangle_base
        self.__triangle_height = triangle_height
        self.__side_length_a = side_length_a
        self.__side_length_b = side_length_b

    def area_of_figure(self):
        return (1 / 2) * self.__triangle_base * self.__triangle_height

    def perimeter_of_figure(self):
        return self.__triangle_base + self.__side_length_a + self.__side_length_b


class Rhomb(Figure):
    def __init__(self, diagonal_1, diagonal_2, side_length):
        self.__diagonal_1 = diagonal_1
        self.__diagonal_2 = diagonal_2
        self.__side_length = side_length

    def area_of_figure(self):
        return (self.__diagonal_1 * self.__diagonal_2) / 2

    def perimeter_of_figure(self):
        return self.__side_length * 4

figures = [Rectangle(4,2), Triangle(5, 7, 8,
                                    8), Rhomb(8, 5, 9)]
for figure in figures:
    print(f'Figure: {figure.__class__.__name__}\nSquare: {figure.area_of_figure()}\nPerimeter: {figure.perimeter_of_figure()}\n')