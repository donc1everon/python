import copy_hw05_easy as hw

param = {
    'mkdir': hw.make_dir,
    'rmdir': hw.del_dir,
    'lsdir': hw.list_dir,
    'cpfile': hw.copy_file,
}

try:
    dir_name = hw.sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = hw.sys.argv[1]
except IndexError:
    key = None
if key:
    if param.get(key):
        param[key](dir_name)
    else:
        print("Задан неверный ключ")



