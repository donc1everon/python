# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.AB = round(math.sqrt(abs((point_b[0] - point_a[0]) ^ 2 + (point_b[1] - point_a[1]) ^ 2)), 2)
        self.AC = round(math.sqrt(abs((point_c[0] - point_a[0]) ^ 2 + (point_c[1] - point_a[1]) ^ 2)), 2)
        self.BC = round(math.sqrt(abs((point_c[0] - point_b[0]) ^ 2 + (point_c[1] - point_b[1]) ^ 2)), 2)

    def find_perimetr(self):
        self.perimetr = (self.AB + self.AC + self.BC)
        return self.perimetr

    def find_square(self):
        self.semi_p = (self.AB + self.AC + self.BC) / 2
        self.square = round(math.sqrt(self.semi_p * (self.semi_p - self.AB) * (self.semi_p - self.AC) *
                                      (self.semi_p - self.BC)), 2)
        return self.square

    def find_height(self):
        self.height = round((self.square * 2 / self.AC), 2)
        return self.height


triangle1 = Triangle((1, 2), (3, 3), (2, 5))
print(triangle1.AB, triangle1.AC, triangle1.BC, triangle1.find_square(), triangle1.find_height(),
      triangle1.find_perimetr())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.