﻿def output_sym(string, sym_lst, result_lst):
    index = ''
    for el in string:
        for az in sym_lst:
            if el != az:
                continue
            elif index == '':
                el = ''
            else:
                result_lst.append(index)
                el = ''
                index = ''
        index += el
    result_lst.append(index)
    return result_lst


print(' Задание-1:\n'.center(55))
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import re
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
# Способ № 1
result_re = re.findall(r'[^A-Z]+', line)

# Способ № 2
AZ_lst = list(map(chr, range(ord('A'), ord('Z')+1)))
result_2 = []

print('Символы в нижнем регистре ПРИ помоще re -', result_re)
print('Символы в нижнем регистре БЕЗ помоще re -', output_sym(line, AZ_lst, result_2))


print('\n', 'Задание-2:\n'.center(55))
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Способ № 1
result_re = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)

# Способ № 2
az_lst = list(map(chr, range(ord('a'), ord('z')+1)))
some_lst = []
result_2 = []
i = 0

output_sym(line_2, az_lst, some_lst)

while len(some_lst) > i:
    # находим в списке положение первого символа элемента состоящего из символов в верхнем регистре
    j = line_2.find(some_lst[i])
    # находим длину элемента
    len_up_lit = len(some_lst[i])
    # два символа в нижнем регистре до
    low_lit = line_2[(j-2):j]
    # два символа в верхнем регистре после
    up_lit = line_2[(j+len_up_lit-2):(j+len_up_lit)]
    # отделяем от двух символов в верхнем регистре в конце элемента
    some_lst[i] = line_2[j:(j + len_up_lit - 2)]
    # проверяем условие задачи
    if low_lit.islower() & up_lit.isupper():
        result_2.append(some_lst[i])
    i += 1
# удаляем пустые строки
result_2 = [el for el in result_2 if el != '']

print('Символы в нижнем регистре ПРИ помоще re -', result_re)
print('Символы в нижнем регистре БЕЗ помоще re -', result_2)


print('\n', 'Задание-3:\n'.center(55))
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import os

path = os.path.join('', 'some.txt')

string = ''
lst = []

my_file = open("some.txt", "w")

while len(lst) < 2500:
    for _ in range(500):
        lst.append(random.randint(0, 9))
for el in lst:
    string = string + str(el)

my_file.write(string)
my_file.close()

num_from_file = 0
repeat = 1
repeat_lst = []
pos_lst = []

with open(path, 'r', encoding='UTF-8') as f:
    for el in f:
        num_from_file = el
# ищем в строке все одинковые последовательности
for i in range(1, 2500):
        if num_from_file[i] == num_from_file[i-1]:
            repeat += 1
        else:
            if repeat > 1:
                # длины одинаковых последовательностей и их позиции заносим в списки
                repeat_lst.append(repeat)
                pos_lst.append(i)
            repeat = 1
# находим максимальное количество повторов
max_rep = max(repeat_lst)
# выводим самую длинную последовательность одинаковых цифр
for i in range(0, len(repeat_lst)):
    if repeat_lst[i] == max_rep:
        print(num_from_file[pos_lst[i] - repeat_lst[i]:pos_lst[i]])




