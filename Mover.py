from utilities import *


class Mover():
    def __init__(self, OD_name, password='000000'):
        self.EOD_path, self.OD_path = make_dir(OD_name)
        self.password = password

    def encrypt(self, path):
        dir_path, filename = os.path.split(path)
        dst_path = os.path.join(dir_path.replace(self.EOD_path, self.OD_path), filename + ".encrypted")
        with open(path, "rb") as src_file:
            with open(dst_path, "wb") as dst_file:
                count = 0
                for line in src_file:
                    for now_byte in line:
                        new_byte = now_byte ^ ord(self.password[count % len(self.password)])
                        count += 1
                        dst_file.write(bytes([new_byte]))
        return dst_path

    def decrypt(self, path):
        dir_path, filename = os.path.split(path)
        dst_path = os.path.join(dir_path.replace(self.OD_path, self.EOD_path), filename[:-10])
        with open(path, "rb") as src_file:
            with open(dst_path, "wb") as dst_file:
                count = 0
                for line in src_file:
                    for now_byte in line:
                        new_byte = now_byte ^ ord(self.password[count % len(self.password)])
                        count += 1
                        dst_file.write(bytes([new_byte]))
        return dst_path

    def update_OD(self):
        # praperation
        EOD_file_list, EOD_dir_list = get_content(self.EOD_path)
        OD_file_list, OD_dir_list = get_content(self.OD_path)

        # update OD directories
        for EOD_dir in EOD_dir_list:
            OD_dir = EOD_dir.replace(self.EOD_path, self.OD_path)
            if not os.path.exists(OD_dir):
                os.makedirs(OD_dir)

        # update OD files
        for EOD_file_path in EOD_file_list:
            OD_file_path = EOD_file_path.replace(self.EOD_path, self.OD_path) + ".encrypted"
            if OD_file_path not in OD_file_list:
                print(self.encrypt(EOD_file_path))

        # delete extra OD files
        for OD_file_path in OD_file_list:
            EOD_file_path = OD_file_path.replace(self.OD_path, self.EOD_path)[:-10]
            if EOD_file_path not in EOD_file_list:
                try:
                    os.remove(OD_file_path)
                except Exception as e:
                    print(e)

        # delete extra dirs
        for OD_dir in OD_dir_list:
            EOD_dir = OD_dir.replace(self.OD_path, self.EOD_path)
            if not os.path.exists(EOD_dir):
                shutil.rmtree(OD_dir)

    def update_EOD(self):
        # preparation
        EOD_file_list, EOD_dir_list = get_content(self.EOD_path)
        OD_file_list, OD_dir_list = get_content(self.OD_path)

        # update EOD directories
        for OD_dir in OD_dir_list:
            EOD_dir = OD_dir.replace(self.OD_path, self.EOD_path)
            if not os.path.exists(EOD_dir):
                os.makedirs(EOD_dir)

        # update EOD files
        for OD_file_path in OD_file_list:
            EOD_file_path = OD_file_path.replace(self.OD_path, self.EOD_path)[:-10]
            if EOD_file_path not in EOD_file_list:
                try:
                    print(self.decrypt(OD_file_path))
                except Exception as e:
                    print(e)

        # delete extra EOD files
        for EOD_file_path in EOD_file_list:
            OD_file_path = EOD_file_path.replace(self.EOD_path, self.OD_path) + ".encrypted"
            if OD_file_path not in OD_file_list:
                try:
                    os.remove(EOD_file_path)
                except Exception as e:
                    print(e)

        # delete extra dirs
        for EOD_dir in EOD_dir_list:
            OD_dir = EOD_dir.replace(self.EOD_path, self.OD_path)
            if not os.path.exists(OD_dir):
                shutil.rmtree(EOD_dir)