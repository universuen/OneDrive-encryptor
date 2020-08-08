from utilities import *


class Mover():
    def __init__(self, OD_name, password):
        if password == '':
            password = '000000'
        self.EOD_path, self.OD_path = make_dir(OD_name)
        self.password = password
        self.hash_dict = {}

    def _encrypt(self, path):
        dir_path, filename = os.path.split(path)
        dst_path = os.path.join(dir_path.replace(self.EOD_path, self.OD_path), filename + ".encrypted")
        with open(path, "rb") as file:
            src_hash = sha1(file.read()).hexdigest()
        with open(path, "rb") as src_file:
            with open(dst_path, "wb") as dst_file:
                count = 0
                for line in src_file:
                    for now_byte in line:
                        new_byte = now_byte ^ ord(self.password[count % len(self.password)])
                        count += 1
                        dst_file.write(bytes([new_byte]))
        with open(dst_path, "rb") as file:
            dst_hash = sha1(file.read()).hexdigest()
            print(dst_hash)
        self.hash_dict[src_hash] = dst_hash
        return dst_path

    def _decrypt(self, path):
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

    def update_online_files(self):
        # preparation
        EOD_file_list, EOD_dir_list = get_content(self.EOD_path)
        EOD_file_hash = get_file_hash(EOD_file_list)
        OD_file_list, OD_dir_list = get_content(self.OD_path)
        OD_file_hash = get_file_hash(OD_file_list)

        # update OD directories
        for EOD_dir in EOD_dir_list:
            OD_dir = EOD_dir.replace(self.EOD_path, self.OD_path)
            if not os.path.exists(OD_dir):
                os.makedirs(OD_dir)

        # update OD files
        for i in EOD_file_hash.items():
            file_path = i[0]
            hash = i[1]
            try:
                if hash not in self.hash_dict.keys():
                    print(self._encrypt(file_path))
                elif self.hash_dict[hash] not in OD_file_hash.values():
                    print(self._encrypt(file_path))
            except Exception as e:
                print(e)

        # delete extra OD files
        for i in OD_file_hash.items():
            file_path = i[0]
            hash = i[1]
            try:
                if hash not in self.hash_dict.values():
                    os.remove(file_path)
                elif get_key(self.hash_dict, hash) not in EOD_file_hash.values():
                    os.remove(file_path)
            except Exception as e:
                print(e)

        # delete extra OD dirs
        for OD_dir in OD_dir_list:
            EOD_dir = OD_dir.replace(self.OD_path, self.EOD_path)
            if not os.path.exists(EOD_dir):
                shutil.rmtree(OD_dir)

    def update_local_files(self):
        # preparation
        EOD_file_list, EOD_dir_list = get_content(self.EOD_path)
        EOD_file_hash = get_file_hash(EOD_file_list)
        OD_file_list, OD_dir_list = get_content(self.OD_path)
        OD_file_hash = get_file_hash(OD_file_list)

        # update EOD directories
        for OD_dir in OD_dir_list:
            EOD_dir = OD_dir.replace(self.OD_path, self.EOD_path)
            if not os.path.exists(EOD_dir):
                os.makedirs(EOD_dir)

        # update EOD files
        for i in OD_file_hash.items():
            file_path = i[0]
            hash = i[1]
            try:
                if get_key(self.hash_dict, hash) not in EOD_file_hash.values():
                    print(self._decrypt(file_path))
            except Exception as e:
                print(e)

        # delete extra EOD files
        for i in EOD_file_hash.items():
            file_path = i[0]
            hash = i[1]
            try:
                if hash not in self.hash_dict.keys():
                    os.remove(file_path)
                elif self.hash_dict[hash] not in OD_file_hash.values():
                    os.remove(file_path)
            except Exception as e:
                print(e)

        # delete extra EOD dirs
        for EOD_dir in EOD_dir_list:
            OD_dir = EOD_dir.replace(self.EOD_path, self.OD_path)
            if not os.path.exists(OD_dir):
                shutil.rmtree(EOD_dir)