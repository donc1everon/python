# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import sys
import hw05_easy as hw05

print('Что вы хотите сделать с папками текущей директории:')
print('1. Перейти в папку ')
print('2. Просмотреть содержимое текущей папки ')
print('3. Удалить папку ')
print('4. Создать папку ')
choise = int(input('Введите число: '))

if choise == 1:
    dir_path = input('Введите название папки: ')
    if not dir_path:
        print('Пустое значение')
    try:
        os.chdir(dir_path)
        print(f'Успешно перешли в папку {dir_path}')
    except FileNotFoundError:
        print('Такой папки нет в данной директории')
if choise == 2:
    hw05.list_dir()
if choise == 3:
    dir_name = input('Введите название папки: ')
    hw05.del_dir(dir_name)
if choise == 4:
    dir_name = input('Введите название папки: ')
    hw05.make_dir(dir_name)