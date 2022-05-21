import subprocess
import sys

from func import *
from errors import *

class Utils:
    def __init__(self):
        self.root = get_root_dir()
        self.zipp_dir = path.join(self.root, 'content\zipps')
        self.wiki_dir = path.join(self.root, 'content\wiki')

        # Check structure consistency
        if not path.exists(self.zipp_dir):
            raise DirectoryConsistencyError(self.zipp_dir)
        elif not path.exists(self.wiki_dir):
            raise DirectoryConsistencyError(self.wiki_dir)


    def get_zipp_list(self):
        zipp_list = []
        # Get only folders
        for name in os.listdir(self.zipp_dir):
            if path.isdir(path.join(self.zipp_dir, name)):
                zipp_list.append(name)
        return zipp_list


    def start_zipp(self, zipp_name):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_name)
        if path.exists(user_zipp_dir):
            start_file_path = path.join(user_zipp_dir, "Start.py")

            # Safe execute Start.py script (probably it's unsafe)
            try:
                subprocess.call([sys.executable, start_file_path])
                # os.system(f'python {path.join(user_zipp_dir, "Start.py")}')
                # exec(open(path.join(user_zipp_dir, "Start.py")).read())
            except:
                raise CorruptedZippError(start_file_path)
        else:
            raise NoSuchZippError(zipp_name)


    def delete_zipp(self, zipp_name):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_name)
        if path.exists(user_zipp_dir):
            os.remove(user_zipp_dir)
        else:
            raise NoSuchZippError(zipp_name)


    def add_zipp(self, zipp_name):
        # Check if this zipp package already exists
        user_zip_list = self.get_zipp_list()
        if zipp_name not in user_zip_list:

            """

            Loading Zipp package....

            """

            pass
        else:
            raise ZippConflictError(zipp_name)

