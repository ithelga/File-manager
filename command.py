import sys

from features import create_folder, create_file, delete, write_to_file, read_file, rename, copy, move, get_list, help, \
    info, change_root, change_dir_up, change_dir_down


class Command(object):
    def __init__(self, function):
        self.function = function

    def execute(self, argv):
        check = CheckArgv(argv)
        if check.is_rigth(self.function):
           return self.function(*argv)
        else:
            print("Неверные аргументы")
            return None


class CheckArgv(object):
    def __init__(self, argv):
        self.argv = argv

    def is_rigth(self, function_name):
        return ARGV_REQ[function_name](len(self.argv))


ARGV_REQ = {
    create_folder: lambda x: True if x == 1 else False,
    create_file: lambda x: True if 3 > x > 0 else False,
    delete: lambda x: True if x == 1 else False,
    write_to_file: lambda x: True if x == 2 else False,
    read_file: lambda x: True if x == 1 else False,
    rename: lambda x: True if x == 2 else False,
    copy: lambda x: True if x == 2 else False,
    move: lambda x: True if x == 2 else False,
    help: lambda x: True if x == 0 else False,
    info: lambda x: True if x == 1 else False,
    change_root: lambda x: True if x == 1 else False,
    change_dir_up: lambda x: True if x == 0 else False,
    change_dir_down: lambda x: True if x == 1 else False,
    get_list: lambda x: True if 4 > x > -1 else False,
}
