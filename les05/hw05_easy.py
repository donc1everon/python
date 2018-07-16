# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil
print('sys.argv = ', sys.argv)

def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.mkdir(dir_name)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def make_n_dir(dir_name):
    for i in range(1, 10):
        dir_name_i = dir_name + '_' + str(i)
        make_dir(dir_name_i)
    dir_name_i = ''

def del_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.rmdir(dir_name)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директории {} уже не существует'.format(dir_name))

def del_n_dir(dir_name):
    for i in range(1, 10):
        dir_name_i = dir_name + '_' + str(i)
        del_dir(dir_name_i)
    dir_name_i = ''

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    list = os.listdir()
    dir_n = 0
    for i in list:
        if os.path.isdir(i):
            print(i)
            dir_n += 1
    if dir_n == 0:
        print('Папок в текущей директории нет!')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    shutil.copyfile(sys.argv[0], 'copy_' + sys.argv[0])