from os import listdir
from os.path import dirname, abspath, join, isfile


INPUT_DIR = join(dirname(dirname(abspath(__file__))), 'input')
DESTINATION_IP = '192.168.1.45'


def get_files(input_dir=INPUT_DIR):
    return [
        item for item in listdir(input_dir) if isfile(join(input_dir, item))
    ]


def get_files_contents(files, input_dir=INPUT_DIR):
    return {file: read_file(join(input_dir, file)) for file in files}


def read_file(file_path):
    with open(file_path) as file:
        return file.read()
