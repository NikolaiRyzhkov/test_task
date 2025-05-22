from sys import argv
from git import Repo
from datetime import datetime
import os
import json
import time
import shutil



WORK_DIR = os.path.dirname(os.path.abspath(argv[0]))

def dowlan_rep(rep_url: str, dir_path: str, version: str) -> str:
    dir_name = rep_url.split('/')[-1] + version
    data_path = WORK_DIR + '/' + dir_name
    Repo.clone_from(rep_url, data_path)     #dowland the repository

    print(datetime.now(), 'The repository was loaded')
    return dir_name


def del_not_target_data(path_dir_for_cline: str, path_safe_dir: str) -> None:   #Removing all files except selected
    
    full_path_dir_for_cline = WORK_DIR + '/' + path_dir_for_cline + '/'

    for title_dir in os.listdir(full_path_dir_for_cline):
        full_path_curent_dir = full_path_dir_for_cline + title_dir
        if os.path.isdir(full_path_curent_dir) and title_dir != path_safe_dir.split('/')[0]:
            os.system('rmdir /S /Q "{}"'.format(full_path_curent_dir))
            print(datetime.now(), full_path_dir_for_cline, 'removed')
    

def sort_file(list_file: list, extensions: list) -> list:    #Search for expansion files
    sort_list = list()
    for file in list_file:
        if file.endswith(extensions):
            sort_list += [file]
    
    return sort_list


def make_server_file(path: str, version: str, extensions: tuple, name: str ='hello world') -> None:     #create server file
    list_files = sort_file(os.listdir(path), extensions)
    data = {'name': name, 'version': version, 'files': list_files}
    file_name = path + 'version.json'
    with open(file_name, 'w') as file:
        json.dump(data, file) 

    print(datetime.now(), 'version.json created')


def zip_directory(path: str) -> None:
    # making name
    name_zip = path.split('/')
    if name_zip[-1] == '':
        name_zip = name_zip[-2]
    else:
        name_zip = name_zip[-1]
    name_zip = name_zip + time.strftime('%d%m%Y')

    shutil.make_archive(name_zip, 'zip', path)

    print(datetime.now(), path, 'is archived')




if __name__ == '__main__':
    rep_url, dir_path, version = argv[1:]

    name_dowland_rep = dowlan_rep(rep_url, dir_path, version)   #dowland rep

    del_not_target_data(name_dowland_rep, dir_path)     #removal of deritors except the source code

    path_src= WORK_DIR + '/' + name_dowland_rep + '/src/app/'       #path to the source code
    
    # create server file
    extensions = ('.py', '.js', '.sh')      
    make_server_file(path_src, version, extensions)

    zip_directory(path_src)
