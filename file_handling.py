import os
import sys
import pathlib
from pathlib import Path
def recursive_dir_search(dir_path):

    all_paths = [dir_path]
    seen = set()
    paths = []
    while all_paths:

        path = all_paths.pop(0)

        if pathlib.Path.is_dir(Path(path)):
            for file in pathlib.Path(path).iterdir():
                if pathlib.Path.is_file(file):
                    paths.append(file)
                    seen.add(file)
                else:
                    all_paths.append(file)
                    paths.append(file)
                    seen.add(file)


    return paths

if __name__ == "__main__":
    paths = recursive_dir_search(sys.argv[1])
    print pathlib.Path
    print sys.path
    print sys.version
    print sys.version_info
    print sys.api_version
    print paths





