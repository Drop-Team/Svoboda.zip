import os
import os.path as path

def get_root_dir():
    cwd = os.getcwd()
    # Get root dir (2 lvl up)
    root_dir = path.join(path.abspath(path.join(cwd, "../..")), )
    return root_dir