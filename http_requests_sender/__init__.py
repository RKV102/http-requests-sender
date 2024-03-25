from os import listdir
from os.path import dirname, abspath, join, isfile


INPUT_DIR = join(dirname(dirname(abspath(__file__))), 'input')
DESTINATION_IP = '192.168.1.45'


def get_files(input_dir=INPUT_DIR):
    items = [join(input_dir, item) for item in listdir(input_dir)]
    return [item for item in items if isfile(item)]


def get_file_contents(file_paths):
    contents = []
    for file_path in file_paths:
        with open(file_path) as file:
            contents.append(file.read())
    return contents
