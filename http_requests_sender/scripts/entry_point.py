from http_requests_sender import (get_files_paths, get_files_contents,
                                  DESTINATION_IP, FIRST_REQUEST_NUM,
                                  LAST_REQUEST_NUM)
from http_requests_sender.http_requests_sender import send_http_requests


def main():
    files_paths = get_files_paths()
    contents = get_files_contents(files_paths)
    send_http_requests(contents, DESTINATION_IP,
                       FIRST_REQUEST_NUM, LAST_REQUEST_NUM)


if __name__ == '__main__':
    main()
