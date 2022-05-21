import subprocess
from os import path
import shutil

from .errors import *
from .func import *


class Utils:
    def __init__(self):
        self.root = get_root_dir()
        self.zipp_dir = path.join(self.root, 'zipps')
        self.wiki_dir = path.join(self.root, 'wiki')

        # Check structure consistency
        if not path.exists(self.zipp_dir):
            raise DirectoryConsistencyError(self.zipp_dir)
        elif not path.exists(self.wiki_dir):
            raise DirectoryConsistencyError(self.wiki_dir)


    def get_zipps_list(self):
        zipp_list = []
        # Get only folders
        for name in os.listdir(self.zipp_dir):
            if path.isdir(path.join(self.zipp_dir, name)):
                zipp_list.append(self.get_zipp_data(name))
        return zipp_list


    def get_zipp_data(self, zipp_directory) -> dict:
        with open(path.join(self.zipp_dir, zipp_directory, "manifest.json")) as f:
            data = json.load(f)
        result = {
            "name": data.get("name"),
            "description": data.get("description"),
            "type": data.get("type"),
            "version": data.get("version"),
            "icon": zipp_directory + "/" + data.get("icon"),
            "size": get_human_readable_size(path.join(self.zipp_dir, zipp_directory)),
            "directory_name": zipp_directory
        }
        return result


    def start_zipp(self, zipp_directory):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_directory)
        if path.exists(user_zipp_dir):
            start_file_path = path.join(user_zipp_dir, "start.sh")

            # Safe execute start.sh script
            try:
                subprocess.Popen(start_file_path, shell=True, cwd=user_zipp_dir, start_new_session=True)
            except Exception as e:
                raise CorruptedZippError(start_file_path)
        else:
            raise NoSuchZippError(zipp_directory)


    def delete_zipp(self, zipp_directory):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_directory)
        if path.exists(user_zipp_dir):
            shutil.rmtree(user_zipp_dir)
        else:
            raise NoSuchZippError(zipp_directory)


    def add_zipp(self, zipp_directory):
        # Check if this zipp package already exists
        user_zip_list = self.get_zipps_list()
        if zipp_directory not in user_zip_list:
            # Loading Zipp package....
            pass
        else:
            raise ZippConflictError(zipp_directory)
