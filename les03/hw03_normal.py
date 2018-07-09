# Задание-1:
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
        row_fibanacci[i] = row_fibanacci[i-1] + row_fibanacci[i-2]
    while n > 0:
        n -= 1
        row_fibanacci.pop(n)
    return row_fibanacci

print(fibonacci(n, m))
# Задача-2:
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

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.