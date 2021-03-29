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
            shutil.rmtree(name, ignore_errors=True)
            if text1 == None:
                print("Папка успешно удалена")
            else:
                print(str(text1) + " Папка успешно удалена")
        else:
            os.remove(name)
            if text2 == None:
                print("Файл успешно удален")
            else:
                print(str(text2) + " Файл успешно удален")
    else:
        print("Не удается найти заданный путь")


def write_to_file(name, text):
    name = str((get_dir().joinpath(pathlib.Path(name))))
    try:
        with open(name, 'w', encoding='utf-8') as file:
            file.write(text)
    except FileNotFoundError:
        print("Такой файл не существует")


def read_file(name):
    name = str((get_dir().joinpath(pathlib.Path(name))))
    try:
        with open(name, "r") as f:
            for line in f.readlines():
                print(line)
    except FileNotFoundError:
        print("Такой файл не существует")


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

    except FileNotFoundError:
        print("Неверно задан путь")

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
        new_name = root.joinpath(pathlib.Path(new_name))
    else:
        new_name = dir.joinpath(pathlib.Path(new_name))

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
    if 3 > int(param) < 0 or 1 > int(param2) < 0:
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
        list_file.sort(key=lambda item: item[int(param)], reverse=True if int(param2) == 1 else False)
        file_pr = ''
        title = f' {"Название файла":30} | {"Размер":8} | {"Дата создания":26} | {"Дата модификации":26}'
        line = 25 * "----"

        for name, size, time_start, time_modification in list_file:
            file_pr += ''.join(
                f' {name:30} | {size:8} | {datetime.fromtimestamp(time_start)} | {datetime.fromtimestamp(time_modification)} \n')
        print(title + "\n" + line + "\n" + file_pr)


def help():
    print(
        f' Расшифровка: \n'
        f' Обяз! - обязательно \n'
        f' Опц - опционально \n'
        f' \n В файле setting.txt хранится root\n'
        f' \n В файле log.txt хранится информация о скрипте\n'

        f' ОСНОВНЫЕ ВОЗМОЖНОСТИ: \n'
        f' create_file - создать файл; 1 арг(обяз!) - имя файла, 2 арг - текс для записи \n'
        f' create_folder - создать директорию; 1 арг(обяз!) - имя директории, \n'
        f' delete - удалить файл или директорию; 1 арг(обяз!) - имя файла или директории для удаления \n'

        f' write_to_file - записать в файл; 1 арг(обяз!) - имя файла или путь к файлу, в который нужно записать, 2 арг(обяз!) - текст сообщения \n'
        f' read_file - прочитать файл; 1 арг(обяз!) - имя файла или путь к файлу, который нужно прочитать \n'
        f' rename - переименовать файл или директорию; 1 арг(обяз!) - имя файла или директории, которые нужно переименовать, 2 арг(обяз!) - имя, на которое заменить \n'
        f' copy - скопировать файл или директорию; 1 арг(обяз!) - имя файла или директории, которые нужно скопировать, 2 арг(обяз!) - имя директории/путь, куда скопировать \n'
        f' move - переместить файл или директорию; 1 арг(обяз!) - имя файла или директории, которые нужно переместить, 2 арг(обяз!) - имя директории/путь, куда переместить \n'

        f' help - помощь; \n'
        f' change_root - сменить корневую директорию; 1 арг(обяз!) - указать абсолютный путь до новой корневой директории \n'
        f' change_dir_up - перейти в родительскую директорию; без аргументов \n'
        f' change_dir_down - перейти в дочернюю директорию; 1 арг(обяз!) - имя папки в текущей директории или путь (абсолютный от корневой или относительный от текуще директории) \n'
        f' list - получить список файлов в каталоге; 1 арг(опц) - имя каталога в текущей директории, если не указать, то список файлов в текущей директории , '
        f' 2 арг (опц) - параметр для сортировки, т.е по какому полю сортировать: 0 - название файла, 1 - Размер, 2 - Дата создания, 3 - Дата Модификации '
        f' 3 арг (опц) - параметр для сортировки: 0 - возрастание, 1 - убывание\n'
    )


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
    root = get_root()
    if dir == root:
        print("Вы достигли корневой директории")
    else:
        new_dir = dir.parents[0]
        with open("dir.txt", 'w', encoding='utf-8') as file:
            file.write(str(new_dir))


def start():
    if os.path.exists("setting.txt") == False or os.path.getsize("setting.txt") == 0:
        way = pathlib.Path(r'C:\Users\otete\PycharmProjects\ IT Python')
        with open("setting.txt", 'w', encoding='utf-8') as file:
            file.write(str(way))
        with open("dir.txt", 'w', encoding='utf-8') as file:
            file.write(str(way))
