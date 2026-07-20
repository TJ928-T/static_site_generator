import os
import shutil




def clean_directory(path):
    if os.path.exists(path) == True:
        shutil.rmtree(path)
    os.mkdir(path)

def copy_files_dir(src_path, new_dir):
    if os.path.isdir(src_path):
        src_paths = os.listdir(src_path)
    def check_paths(src, src_paths, new_dir):
        for path in src_paths:
            file_path = os.path.join(src, path)
            if os.path.isfile(file_path):
                shutil.copy(file_path, new_dir)
                print(f"Copied '{file_path}' to '{new_dir}'")
            if os.path.isdir(file_path):
                dir = f"{new_dir}/{path}"
                os.mkdir(dir)
                print(f"Created new directory '{dir}'")
                dir_paths = os.listdir(file_path)
                check_paths(file_path, dir_paths, dir)
    check_paths(src_path, src_paths, new_dir)