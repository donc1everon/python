# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import random

SURNAME = ('Сидоров', 'Иванов', 'Петров', 'Васечкин', 'Захаров', 'Сидорова', 'Иванова', 'Петрова', 'Захарова')
NAME = ('А.', 'Б.', 'В.', 'Г.', 'Д.', 'Е.', 'З.', 'И.', 'К.', 'Л.', 'М.', 'Н.', 'О.', 'П.', 'Р.', 'С.')
SUBJECT = ('математика', 'русский', 'английский', 'физика', 'Информатика', 'химия', 'биология')



class School:
    def __init__(self, name):
        self.name = name
        self.classes = []

    # добавляем класс в школу
    def add_class(self, class_):
        self.classes.append(class_)

    # получаем полный список всех классов
    def all_class(self):
        print(f'Полный список классов в школе {self.name}:')
        for cla in self.classes:
            print(f'Class {cla.name}')

    # получаем список всех учеников в классе
    def all_students(self, name):
        for student in self.classes:
            if student.name == name:
                student.all_students()

    # Ученик --> Класс --> Учителя --> Предметы
    def student_items(self, name):
        for cla in self.classes:
            for student in cla.students:
                if student.name == name:
                    for teacher in cla.teachers:
                        print(f'\tУченик - {student.name} | класс - {cla.name} | преподаватель - {teacher.name}\t | '
                              f'предмет - {teacher.subject}')

    # Получаем ФИО родителей указанного ученика
    def my_parent(self, name):
        for cla in self.classes:
            print(cla)
            for student in cla.students:
                print(student)
                if student.name == name:
                    student.my_parent()

    # Получаем всем учителей в классе
    def all_teacher(self, name):
        for teacher in self.classes:
            if teacher.name == name:
                teacher.all_teacher()

    def generator(self, Classes, Students, Subjects):
        for idx in range(int(Classes)):
            xclass = Class(str(random.randint(1, 11)) + random.choice(('A', 'B', 'C', 'D')))
            self.add_class(xclass)
            for i in range(int(Students)):
                xclass.add_student(Student(random.choice(SURNAME) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(SURNAME) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(SURNAME) + 'а ' + random.choice(NAME) + random.choice(NAME)))
            for i in range(int(Subjects)):
                xclass.add_teacher(random.choice(SURNAME) + ' ' + random.choice(NAME) + random.choice(NAME),
                                  random.choice(SUBJECT))

class Class:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    # добавляем ученика в класс
    def add_student(self, student):
        self.students.append(student)

    # добавляем учителя и предмет, который он ведет, в класс
    def add_teacher(self, name, subject):
        self.teachers.append(Teacher(name, subject))

    # Показываем учеников в классе
    def all_students(self):
        print(f'В классе {self.name} учатся:')
        for student in self.students:
            print(f'ученик {student.name}')

    def all_teacher(self):
        print(f'В классе {self.name} преподают:')
        for teacher in self.teachers:
            print(f'Преподаватель {teacher.name}')


class Student:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    # Показываем родителей ученика
    def my_parent(self):
        print(f'Отец - {self.father}, Мать - {self.mother}')


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject



school = School('Гимназия №2')
school.generator(5, 5, 5)
print('*' * 50)
school.all_class()
# print('-' * 50)
your_class = input("Введите класс: ")
print('-' * 50)
school.all_students(your_class)
print('-' * 50)
your_student = input("Введите Ученика: ")
# print('-' * 50)
# print(f'Информация о {your_student}:')
# school.student_items(your_student)
# print('-' * 50)
print(f'Родители {your_student}:')
school.my_parent(your_student)
# print('-' * 50)
# school.all_teacher(your_class)
