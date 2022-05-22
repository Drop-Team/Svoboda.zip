import signal
import subprocess
import sys
import time
from multiprocessing import Process
from os import path
import shutil
import zipfile

import markdown as markdown

from .errors import *
from .func import *


class Utils:
    def __init__(self):
        self.root = get_root_dir()
        self.zipp_dir = path.join(self.root, 'zipps')
        self.wiki_dir = path.join(self.root, 'wiki')
        self.active_apps = {}

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


    def get_zipp_data(self, zipp_dir) -> dict:
        with open(path.join(self.zipp_dir, zipp_dir, "manifest.json")) as f:
            data = json.load(f)
        result = {
            "name": data.get("name"),
            "description": data.get("description"),
            "type": data.get("type"),
            "version": data.get("version"),
            "icon": zipp_dir + "/" + data.get("icon"),
            "size": get_human_readable_size(path.join(self.zipp_dir, zipp_dir)),
            "directory_name": zipp_dir
        }
        return result


    def get_zipp_markdown(self, zipp_dir):
        md_path = path.join(self.zipp_dir, zipp_dir, "help.md")
        md_html = ''
        # Convert md to html
        try:
            markdown.markdownFromFile(
                input=md_path,
                output=md_html,
                encoding='utf8',
            )
            return md_html
        except Exception:
            raise FileConsistencyError(md_path)


    def start_zipp(self, zipp_dir):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_dir)
        if path.exists(user_zipp_dir):
            start_file_path = path.join(user_zipp_dir, "start.sh")

            # Safe execute start.sh script
            try:
                process = subprocess.Popen(start_file_path, shell=True, cwd=user_zipp_dir, start_new_session=True)
                self.active_apps[zipp_dir] = process

            except Exception as e:
                raise CorruptedZippError(start_file_path)
        else:
            raise NoSuchZippError(zipp_dir)


    def stop_zipp(self, zipp_dir):
        try:
            # Fully terminate process if it exists
            process = self.active_apps[zipp_dir]
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            self.active_apps.pop(zipp_dir)

        except Exception:
            pass



    def delete_zipp(self, zipp_dir):
        # Check if zipp package exists
        user_zipp_dir = path.join(self.zipp_dir, zipp_dir)
        if path.exists(user_zipp_dir):
            shutil.rmtree(user_zipp_dir)
        else:
            raise NoSuchZippError(zipp_dir)


    def add_local_zipp(self, zipp_path):
        zipp_name = (zipp_path.split('/'))[-1].split('.')[0]
        user_zip_list = self.get_zipps_list()

        # Check if this zipp package already exists
        if zipp_name not in user_zip_list:
            # Extract to zipp directory
            with zipfile.ZipFile(zipp_path, 'r') as zip_ref:
                zip_ref.extractall(self.zipp_dir)
            pass
        else:
            raise ZippConflictError(zipp_name)


    def add_net_zipp(self, zipp_name):

        # Download zipp from net
        # Then, add it as local one

        pass


    def restart_app(self):
        run_path = path.join(os.getcwd(), 'run.py')
        try:
            p1 = Process(target=subprocess.call, args=([sys.executable, run_path],))
            p1.start()
            time.sleep(2)
            exit()

        except Exception as e:
            raise CorruptedFileError('run.py', e)
