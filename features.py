# Created by Helga on 28.02.2021
import os
import shutil
import pathlib
from datetime import datetime


def get_dir():
    with open("dir.txt", "r") as f:
        dir = f.readline()
    return pathlib.Path(dir)


def get_root():
    with open("setting.txt", "r") as f:
        root = f.readline()
    return pathlib.Path(root)


def create_folder(name):
    name = str((get_dir()).joinpath(pathlib.Path(name)))
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже существует")
    else:
        print('Папка успешно создана')


def create_file(name, text=None):
    name = str(((get_dir()).joinpath(pathlib.Path(name))))
    with open(name, 'w', encoding='utf-8') as file:
        if text:
            file.write(text)
    print('Файл успешно создан')


def delete(name, text1=None, text2=None):
    name = str(get_dir().joinpath(pathlib.Path(name)))
    if os.path.exists(name):
        if os.path.isdir(name):
            os.rmdir(name)
            print(text1 + "Папка успешно удалена")
        else:
            os.remove(name)
            print(text2 + "Файл успешно удален")
    else:
        print("Не удается найти заданный путь")


def write_to_file(name, text):
    name = str((get_dir().joinpath(pathlib.Path(name))))
    with open(name, 'w', encoding='utf-8') as file:
        file.write(text)


def read_file(name):
    name = str((get_dir().joinpath(pathlib.Path(name))))
    with open(name, "r") as f:
        for line in f.readlines():
            print(line)


def rename(name, new_name):
    dir = get_dir()
    name = dir.joinpath(pathlib.Path(name))
    name_is_dir = os.path.isdir(name)
    new_name = dir.joinpath(pathlib.Path(new_name))
    try:
        os.rename(name, new_name)
    except FileExistsError:
        if name_is_dir:
            print("Такая папка уже существует")
        else:
            print("Такой файл уже существует")
    else:
        if name_is_dir:
            print("Папка успешно переименована")
        else:
            print("Файл успешно переименован")


def copy(name, new_name, text1="Папка успешно скопирована", text2="Файл успешно скопирован"):
    dir = get_dir()
    root = get_root()
    listdir = os.listdir(dir)
    name_exists = False
    newName_exists = False
    for file in listdir:
        if file == name:
            name_exists = True
        elif file == new_name:
            newName_exists = True
        if newName_exists and name_exists:
            break

    if name_exists == False:
        name = str(root.joinpath(pathlib.Path(name)))
    else:
        name = str(dir.joinpath(pathlib.Path(name)))

    if newName_exists == False:
        new_name = str(root.joinpath(pathlib.Path(new_name)))
    else:
        new_name = str(dir.joinpath(pathlib.Path(new_name)))

    if os.path.exists(name) and os.path.exists(new_name):
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                "Такая папка уже существует"
            else:
                print(text1)
        else:
            shutil.copy(name, new_name)
            print(text2)
    else:
        print("Не удается найти заданный путь")


def move(name, new_name):
    copy(name, new_name, "Папка успешно перемещена", "Файл успешно перемещен")
    delete(name, "Старая ", "Старый ")


def get_list(name=None, param=0, param2=0):
    if 3 > param < 0 or 1 > param2 < 0:
        print("Переданы неверные параметры")
    else:
        dir = get_dir()
        if name == None:
            name = dir
        else:
            name = dir.joinpath(pathlib.Path(name))
        listdir = os.listdir(name)
        files = []
        for file in listdir:
            filePath = name.joinpath(pathlib.Path(file))
            files.append([file, os.path.getsize(filePath), os.path.getctime(filePath), os.path.getmtime(filePath)])
        list_file = files[:]
        list_file.sort(key=lambda item: item[int(param)], reverse=True if param2 == 1 else False)
        file_pr = ''
        title = f' {"Название файла":30} | {"Размер":8} | {"Дата создания":26} | {"Дата модификации":26}'
        line = 25 * "----"

        for name, size, time_start, time_modification in list_file:
            file_pr += ''.join(
                f' {name:30} | {size:8} | {datetime.fromtimestamp(time_start)} | {datetime.fromtimestamp(time_modification)} \n')
        print(title + "\n" + line + "\n" + file_pr)


def help():
    pass


def info(text):
    with open('log.txt', 'a', encoding='utf-8') as file:
        time = datetime.now()
        file.write(f'{text} в {time}\n')


def change_root(way_to_root):
    with open('setting.txt', 'w', encoding='utf-8') as file:
        file.write(way_to_root)
    with open('dir.txt', 'w', encoding='utf-8') as file:
        file.write(way_to_root)
    info("Корневая директория была изменена")
    print("Корневая директория была изменена")


def change_dir_down(way):
    dir = get_dir()
    way = str(dir.joinpath(pathlib.Path(way)))
    if os.path.isdir(way):
        with open("dir.txt", 'w', encoding='utf-8') as file:
            file.write(way)
    else:
        print("Неверно задано имя папки")


def change_dir_up():
    dir = get_dir()
    new_dir = str(dir.parents[0])
    if new_dir == str(get_root()):
        print("Вы достигли корневой директории")
    else:
        with open("dir.txt", 'w', encoding='utf-8') as file:
            file.write(new_dir)


def start():
    if os.path.exists("setting.txt") == False or os.path.getsize("setting.txt") == 0:
        with open("setting.txt", 'w', encoding='utf-8') as file:
            file.write(r'C:\Users\otete\PycharmProjects\ IT Python\Tasks 4 semester\Practice\file-manager')
    if os.path.exists("dir.txt") == False or os.path.getsize("dir.txt") == 0:
        with open("dir.txt", 'w', encoding='utf-8') as file:
            file.write(r'C:\Users\otete\PycharmProjects\ IT Python\Tasks 4 semester\Practice\file-manager')
