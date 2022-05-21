import os
import json


def get_root_dir():
    cwd = os.getcwd()
    return cwd


def get_human_readable_size(directory_path):
    def get_size(directory_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size


    def human_readable_size(size, decimal_places=2):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0 or unit == 'GB':
                break
            size /= 1024.0
        return f"{size:.{decimal_places}f} {unit}"

    bytes_size = get_size(directory_path)
    return human_readable_size(bytes_size)


def get_config_data():
    root = get_root_dir()
    config = os.path.join(os.path.abspath(os.path.join(root, "../..")), 'config.json')

    # Open JSON file
    f = open(config)
    data = json.load(f)
    return data
