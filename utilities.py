import os
import getpass
import pickle
import shutil


# Get all files and directories' paths
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
    print(file_list)
    print(dir_list)
    return (file_list, dir_list)


def make_dir(OD_name):
    """
    Make encrypted OneDrive directory
    :param OD_name: OneDrive name
    :return: (encrypted OneDrive path, original OneDrive path)
    """
    username = getpass.getuser()
    OD_path = "C:\\Users\\" + username + "\\" + OD_name
    EOD_path = "C:\\Users\\" + username + "\\E-OneDrive"
    if not os.path.exists(EOD_path):
        os.makedirs(EOD_path)
    return EOD_path, OD_path

if __name__ == '__main__':
    encrypt("C:\\Users\\SOBER\\Downloads\\hhh.torrent", "123456")