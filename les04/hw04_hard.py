﻿# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
print("rotate_matrix = ")
rotate_matrix = list(map(print, [list(i) for i in zip(*matrix)]))


print('\n')
# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

num_lst = []
summ_max = 0
for num in number:
    if num != '\n':
        num_lst.append(int(num))

last_5 = len(num_lst) - 4

for i in range(0, last_5):
    summ = 1
    n = 0
    while n < 5:
        summ = summ * num_lst[i+n]
        n += 1
        if summ > summ_max:
            summ_max = summ
            offset_i = i

print(f"Наибольшее произведение пяти последовательных цифр = {summ_max} \n"
      f"Индекс смещения первого числа = {offset_i}")

print('\n')
# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
import copy
lst_coord = []
x_i = 0
y_i = 1

lst_coord = [[1, 3], [2, 7], [3, 2], [4, 8], [5, 5], [6, 1], [7, 4], [8, 6]]    # NO
lst_coord_2 = [[3, 7], [2, 7], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]  # YES
# def enter_coor(lst):
#     n = 1
#     while len(lst) < 8:
#         x = int(input(f'Ввведите координату от 1 до 8 для х{n}: '))
#         y = int(input(f'Ввведите координату от 1 до 8 для y{n}: '))
#         lst.append([x, y])
#         n += 1

# получаем координаты 8 ферзей
# enter_coor(lst_coord)

def check_hit(lst, coord_xi, coord_yi):
    lst_coord_copy = copy.deepcopy(lst)
    for ev in lst_coord_copy:
        repeat = 0
        j = 0
        while j < 8:
            x1 = ev[coord_xi]
            x2 = lst[j][coord_xi]
            y1 = ev[coord_yi]
            y2 = lst[j][coord_yi]
            # проверка не совпадают ли линии по х или у или диагонали ферзей
            if (x1 == x2) | (y1 == y2) | (abs(x1 - x2) == abs(y1 - y2)):
                repeat += 1
            j += 1
        lst_coord_copy.remove(ev)
        if repeat > 1:
             return 'YES'
    return 'NO'

print('При растоновке №1, ферзи бьют друг друга -', check_hit(lst_coord, x_i, y_i))
print('При растоновке №2, ферзи бьют друг друга -', check_hit(lst_coord_2, x_i, y_i))



