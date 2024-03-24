from os import listdir
from os.path import dirname, abspath, join, isfile


INPUT_DIR = join(dirname(dirname(abspath(__file__))), 'input')


def get_files(input_dir=INPUT_DIR):
    items = [join(input_dir, item) for item in listdir(input_dir)]
    return [item for item in items if isfile(item)]


def get_files_content(file_paths):
    contents = []
    for file_path in file_paths:
        with open(file_path) as file:
            contents.append(file.read())
    return contents
