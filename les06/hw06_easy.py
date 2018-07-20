# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.AB = round(math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2), 2)
        self.BC = round(math.sqrt((point_c[0] - point_b[0]) ** 2 + (point_c[1] - point_b[1]) ** 2), 2)
        self.CA = round(math.sqrt((point_a[0] - point_c[0]) ** 2 + (point_a[1] - point_c[1]) ** 2), 2)

    def find_perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return self.perimetr

    def find_square(self):
        self.semi_p = (self.AB + self.CA + self.BC) / 2
        self.square = round(math.sqrt(self.semi_p * (self.semi_p - self.AB) * (self.semi_p - self.BC) *
                                      (self.semi_p - self.CA)), 2)
        return self.square

    def find_height(self):
        self.height = round((self.square * 2 / self.CA), 2)
        return self.height


print('*' * 50)
print('Задание - 1')
print('*' * 50)
triangle1 = Triangle((1, 2), (3, 3), (2, 6))
print(f'Сторона АВ = {triangle1.AB}\nСторона BC = {triangle1.BC}\nСторона CA = {triangle1.CA}\n'
      f'Периметр = {triangle1.find_perimetr()}\nПлощадь = {triangle1.find_square()}\n'
      f'Высота = {triangle1.find_height()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqualTrapezoid:
    def __init__(self, point_a, point_b, point_c, point_d):
        self.a = point_a
        self.b = point_b
        self.c = point_c
        self.d = point_d

    def sides(self):
        self.AB = round(math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2), 2)
        self.BC = round(math.sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2), 2)
        self.CD = round(math.sqrt((self.d[0] - self.c[0]) ** 2 + (self.d[1] - self.c[1]) ** 2), 2)
        self.DA = round(math.sqrt((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2), 2)
        lst_of_sides = [self.AB, self.BC, self.CD, self.DA]
        return lst_of_sides

    def check_on_equal(self):
        self.AC = round(math.sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2), 2)
        self.BD = round(math.sqrt((self.d[0] - self.b[0]) ** 2 + (self.d[1] - self.b[1]) ** 2), 2)

        if self.AC == self.BD:
            return 'Проверка на равнобокость трапеция прошла!'
        else:
            return 'Трапеция не равнобокая!'

    def find_perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CD + self.DA)
        return self.perimetr

    def find_square(self):
        self.square = round((self.BC + self.DA / 2) * math.sqrt(abs(self.AB ** 2 - ((self.DA - self.BC) ** 2 +
                                                                self.AB ** 2 - self.CD ** 2 / 2 * (self.DA -
                                                                                                   self.BC)) ** 2)), 2)
        return self.square


print('*' * 50)
print('Задание - 2')
print('*' * 50)
trapezoid = EqualTrapezoid((1, 1), (2, 2), (5, 2), (6, 1))
print(trapezoid.check_on_equal())
print(f'Сторона AB = {trapezoid.sides()[0]}')
print(f'Сторона BC = {trapezoid.sides()[1]}')
print(f'Сторона CD = {trapezoid.sides()[2]}')
print(f'Сторона DA = {trapezoid.sides()[3]}')
print(f'Периметр = {trapezoid.find_perimetr()}')
print(f'Площадь найденная через 4 стороны = {trapezoid.find_square()}')
