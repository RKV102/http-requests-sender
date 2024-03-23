from csv_converter import get_files, get_files_content
from csv_converter.converter import convert


def main():
    files = get_files()
    contents = get_files_content(files)
    convert(contents)


if __name__ == '__main__':
    main()
