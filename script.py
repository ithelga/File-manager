# Created by Helga on 28.02.2021
from command import Command

import sys
from features import get_list, start, create_file, create_folder, delete, write_to_file, read_file, rename, copy, move, \
    help, info, change_root, change_dir_up, change_dir_down, get_dir
import pathlib
import sys
info('Скрипт начал работу')
start()



cfile = Command(create_file)
cfolder = Command(create_folder)
delete = Command(delete)
wfile = Command(write_to_file)
rfile = Command(read_file)
renamef = Command(rename)
cp = Command(copy)
mv = Command(move)
hp = Command(help)
list = Command(get_list)
chroot = Command(change_root)
chdirup = Command(change_dir_up)
chdirdown = Command(change_dir_down)

MAP = {
    'create_file': cfile,
    'create_folder': cfolder,
    'delete': delete,
    'write_to_file': wfile,
    'read_file': rfile,
    'rename': renamef,
    'copy': cp,
    'move': mv,
    'help': hp,
    'change_root': chroot,
    'change_dir_up': chdirup,
    'change_dir_down': chdirdown,
    'list': list,
}

argv = sys.argv
command = argv[1]
if len(command) > 0:
    if command in MAP:
        MAP[command].execute(argv[2:])

print(get_dir())
info('Скрипт закончил работу')
