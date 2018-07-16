# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.mkdir(dir_name)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copyfile(file_name, 'copy_' + file_name)
        print(f'Файл {file_name} успешно скопирован')
    except FileNotFoundError:
        print(f'Файла с таким именем {file_name} нет в данной директории')


def rm_file():
    if not file_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        answer = ''
        while answer != 'Y' or answer != 'N':
            answer = input(f'Вы уверены, что хотите удалить {file_name}? Y/N ')
            answer = answer.upper()
            if answer == 'Y':
                os.remove(file_name)
                print('файл {} удален'.format(file_name))
            elif answer == 'N':
                print("Действие отменено")
                return
    except FileNotFoundError:
        print('файла {} уже не существует'.format(file_name))


def my_cd():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print(f'Текущая директория - {os.getcwd()}')
    except FileNotFoundError:
        print(f'Директории {file_name} нет здесь!')


def full_ls():
    print(f'Полный путь текущей директории - "{os.getcwd()}"')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": rm_file,
    "cd": my_cd,
    "ls": full_ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None


try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")