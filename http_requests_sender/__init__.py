from os import listdir
from os.path import dirname, abspath, join, isfile
from math import inf


INPUT_DIR = join(dirname(dirname(abspath(__file__))), 'input')
DESTINATION_IP = '192.168.1.45'
FIRST_REQUEST = 1
LAST_REQUEST = inf


def get_files(input_dir=INPUT_DIR):
    for item in listdir(input_dir):
        item_path = join(input_dir, item)
        if isfile(item_path):
            yield item_path


def get_files_contents(files):
    return (read_file(file) for file in files)


def read_file(file_path):
    with open(file_path) as file:
        return file.read()
