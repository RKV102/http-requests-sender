from os import listdir
from os.path import join, isfile


def get_files_paths(input_dir):
    for item in listdir(input_dir):
        item_path = join(input_dir, item)
        if isfile(item_path):
            yield item_path


def get_files_contents(files_paths):
    return (get_file_content(file_path) for file_path in files_paths)


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()
