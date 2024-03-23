from curl_converter import get_files, get_files_content
from curl_converter.converter import convert
from curl_converter.curl import send_curl_requests


def main():
    files = get_files()
    contents = get_files_content(files)
    curl_requests = convert(contents)
    send_curl_requests(curl_requests)


if __name__ == '__main__':
    main()
