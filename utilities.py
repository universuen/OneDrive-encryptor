import os
import getpass
import pickle
import shutil
from hashlib import sha1


def get_content(path):
    """
    Get file list and directory list of the given path
    :param path: str
    :return: (file list, dir list)
    """
    file_list = []
    dir_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            file_list.append(os.path.join(root, name))
        for name in dirs:
            dir_list.append(os.path.join(root, name))
    return (file_list, dir_list)


def get_file_hash(file_path_list):
    """
    Get hashes of all files in the given list
    :param file_path_list: list
    :return: dictionary {file path: hash}
    """
    file_hash = {}
    for file_path in file_path_list:
        try:
            with open(file_path, "rb") as file:
                file_hash[file_path] = sha1(file.read()).hexdigest()
        except Exception as e:
            print(e)
    return file_hash


def make_dir(OD_name):
    """
    Make encrypted OneDrive directory
    :param OD_name: OneDrive name
    :return: (encrypted OneDrive path, original OneDrive path)
    """
    username = getpass.getuser()
    OD_path = "C:\\Users\\" + username + "\\" + OD_name
    if not os.path.exists(OD_path):
        print("Wrong folder name, check and input again.")
        exit()
    EOD_path = "C:\\Users\\" + username + "\\E-OneDrive"
    if not os.path.exists(EOD_path):
        os.makedirs(EOD_path)
    return EOD_path, OD_path


def get_key(dict, value):
    """
    Get the first key of the given value in the given dictionary
    :param dict:dict
    :param value:str
    :return:str
    """
    for item in dict.items():
        if item[1] == value:
            return item[0]
