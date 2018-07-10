print('Задание-1:\n'.center(55))
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

n = int(input("n "))
m = int(input("m "))

def fibonacci(n, m):
    i = 1
    row_fibanacci = [1, 1]
    if n > m:
        return print("Не верный список!")
    while m != i:
        i += 1
        row_fibanacci.append(0)
        row_fibanacci[i] = row_fibanacci[i - 1] + row_fibanacci[i - 2]
    while n > 0:
        n -= 1
        row_fibanacci.pop(n)
    return row_fibanacci

print(fibonacci(n, m))


print('\n', 'Задача-2:\n'.center(55))
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    sort_lst = []
    while len(origin_list) != 0:
        for el in origin_list:
            i = 0
            min_el = el
            for el_1 in origin_list:
                if (el >= el_1) & (min_el >= el_1):
                    min_el = el_1
                    del_el = i
                i += 1
            sort_lst.append(min_el)
            origin_list.pop(del_el)
    print(sort_lst)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


print('\n', 'Задача-3:\n'.center(55))
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

num_lst = [2, 0, 10, -12, 2.5, 20, -11, 4, 4, 0]
str_lst = ['', 'not null', 'bla', '', '10']


def my_filter(fil_func, iter):
    ret_lst = []
    for x in iter:
        if (fil_func(x) == True) or (fil_func(x) != 0):
            ret_lst.append(x)
    return ret_lst


print(my_filter(lambda x: x >= 0, num_lst))
print(my_filter(lambda x: x < 0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(my_filter(lambda x: x == 0, num_lst))
print(my_filter(len, ['', 'not null', 'bla', '', '10']))


print('\n', 'Задача-4:\n'.center(55))
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = ['x1', 'y1']
A2 = ['x2', 'y2']
A3 = ['x3', 'y3']
A4 = ['x4', 'y4']
coor_dic = {}

def check_par(*args):
    j = 1
    for arg in args:
        print('Координаты точки A' + str(j))
        coor_dic[arg[0]] = int(input('Введите координату x' + str(j)))
        coor_dic[arg[1]] = int(input('Введите координату y' + str(j)))
        j += 1
    if (coor_dic['x1'] - coor_dic['x2'] == coor_dic['x4'] - coor_dic['x3']) & \
            (coor_dic['y1'] - coor_dic['y2'] == coor_dic['y4'] - coor_dic['y3']):
        return print('Заданные точки являются вершинами параллелограмма!')
    else:
        return print('ТОчки не являются вершинами параллелограмма!')


check_par(A1, A2, A3, A4)
