# Created by Helga on 28.02.2021
import os
import shutil
import pathlib
from datetime import datetime


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже существует")


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as file:
        if text:
            file.write(text)


def delete(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def write_to_file(name, text):
    with open(name, 'w', encoding='utf-8') as file:
            file.write(text)


def read_file(name):
    with open(name, "r") as f:
        for line in f.readlines():
            print(line)


def rename(name, new_name):
    try:
        os.rename(name, new_name)
    except FileExistsError:
        if os.path.isdir(name):
            print("Такая папка уже существует")
        else:
            print("Такой файл уже существует")


def copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            "Такая папка уже существует"
    else:
        shutil.copy(name, new_name)


def get_list(name, param=0, param2=0):  # сортировка
    listdir = os.listdir(name)
    files = []
    for file in listdir:
        files.append([file, os.path.getsize(file), os.path.getctime(file), os.path.getmtime(file)])
    list_file = files[:]  # копия списока, чтобы не испортить изначальный набор данных
    list_file.sort(key=lambda item: item[param], reverse=True if param2 == 1 else False)
    file_pr = ''
    title = f' {"Название файла":30} | {"Размер":8} | {"Дата создания":26} | {"Дата модификации":26}'
    line = 25 * "_ _ "

    for name, size, time_start, time_modification in list_file:
        file_pr += ''.join(
            f' {name:30} | {size:8} | {datetime.fromtimestamp(time_start)} | {datetime.fromtimestamp(time_modification)} \n')
    print(title + "\n" + line + "\n" + file_pr)



def help():
    pass


def info(text):
    time = datetime.now()
    print(f'{text} в {time}')


def change_root(way_to_root):
    with open('setting.txt', 'w', encoding='utf-8') as file:
        file.write(way_to_root)


def start():
    if os.path.getsize("setting.txt") == 0:
        with open("setting.txt", 'w', encoding='utf-8') as file:
            file.write(r'C:\Users\otete\PycharmProjects\ IT Python\Tasks 4 semester\Practice\file-manager\root')


